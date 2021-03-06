// Save stuff relevant to selections
var selection_url = null;
var separate_on_selection = true;
var listing_list_cache = null;

// <editor-fold desc="event handlers">
/*******************
 *
 * EVENT HANDLERS
 *
 ******************/

var timeoutID = null;
/**
 * Resize listing list container height on widow resize, with 200ms lag.
 */
function on_window_resize() {
    if (timeoutID != null) {
        clearTimeout(timeoutID);
    }

    timeoutID = setTimeout(function() {
        set_container_heights();

        var is_separate = is_detail_separate();
        if ((is_separate && separate_on_selection) || (!is_separate && !separate_on_selection)) {
            return;
        }

        // Expanding past breakpoint
        if (is_separate && !separate_on_selection) {
            separate_on_selection = true;
            load_listings_cached();
        }

        // This is the same regardless if expanded or shrank past breakpoint
        display_listing_detail(is_separate, $(detail_container_name(is_separate)), selection_url);

    }, 200);
}

/**
 * Event handler for filter option change operation.
 */
function filter_changed() {
    var val = $(this).find('option').filter(':selected').val();
    var filter_wrapper = $(this).parent();

    switch(val) {
        case 'all':
            filter_wrapper.find('input').remove();
            filter_wrapper.append('<input type="text" class="form-control filter-input" disabled/>');
            break;
        case 'title':
        case 'isbn':
        case 'class':
            filter_wrapper.find('input').remove();
            filter_wrapper.append('<input type="text" class="form-control filter-input" />');
            break;
    }
}

/**
 * Event handler for selection of a listing from the list.
 */
function listing_selected() {
    var is_separate = is_detail_separate();
    var url = $(this).attr('detail-url');

    selection_url = url;
    separate_on_selection = is_separate;

    $('.listing-list .listing.selection').removeClass('selection');
    $(this).addClass('selection');

    listing_list_cache = $(list_container_name()).html();

    display_listing_detail(is_separate, $(detail_container_name(is_separate)), url);
}

/**
 * Event handler for click on add filter field button.
 */
function add_filter_field() {
    var sel;
    if (is_detail_separate()) {
        sel = '.filter-container .listing-filter-wrapper';
    } else {
        sel = '#filter-modal .listing-filter-wrapper';
    }
    $(sel).append(
        '<div class="listing-filter-group">' +
            '<select class="form-control listing-filter">' +
                '<option value="all">All Books</option>' +
                '<option value="title">Title</option>' +
                '<option value="isbn">ISBN</option>' +
                '<option value="class">Class Code</option>' +
            '</select>' +
        '</div>'
    );

    var lf = $('.listing-filter');
    lf.off('change');
    lf.on('change', filter_changed);
}

function paginate_click() {
    var this_closure = $(this);
    var url = this_closure.find('h4').attr('paginate-data');

    $.get(url, function(data) {
        this_closure.remove();
        var lis = $(data).filter('ul').html();

        $(list_container_name()).find('.listing-list').append(lis);
        connect_listing_click_handler();
        listing_list_cache = $(list_container_name()).html();

        $('li.paginator').on('click', paginate_click);
    });
}


function add_create_form_handler() {
    $('#create-modal').find('form').on('submit', create_form_submitted);
}


function create_form_submitted() {
    var data = $(this).serialize();
    $.post($(this).attr('action'), data, function(data) {
        $('#create-modal').find('.modal-body').html(data);
        add_create_form_handler();
    });

    return false;
}


function xs_filter_click() {
    $('#filter-modal').modal();
}


/*************************
 *
 * End Event Handlers
 *
 *************************/

// </editor-fold>


/**
 * Set listing list and detail container heights to window size - navbar - banner
 */
function set_container_heights() {
    // Window height - navbar height - banner height - filter bar height
    var h = $(window).height() - $('.navbar').height() - $('.banner').height() - $('.filter-container').outerHeight();

    $(list_container_name()).height(h);
    $(detail_container_name(is_detail_separate())).height(h);
}


/**
 * Populate listings list via ajax call.
 */
function load_listings() {
    var filter_group_selector, sort_select_selector;
    if (is_detail_separate()) {
        filter_group_selector = '.filter-container .listing-filter-group';
        sort_select_selector = '.filter-container .listing-sort';
    } else {
        filter_group_selector = '#filter-modal .listing-filter-group';
        sort_select_selector = '#filter-modal .listing-sort';
    }

    // Implemented this way because there can be multiple filter fields on same key
    var stack = [];
    $(filter_group_selector).each(function() {
        var sel = $(this).find('select').find('option').filter(':selected');
        var key = sel.val();

        if (key == 'all') {
            return;
        }

        var value = $(this).find('input').val();
        var o = {};
        o[key] = value;

        stack.push($.param(o));
    });

    stack.push(
        $.param({
            order_by: $(sort_select_selector).find('option').filter(':selected').val()
        })
    );

    var querystring = '';
    if (stack.length > 0) {
        querystring = '?' + stack.join('&');
    }

    $.get(LISTING_LIST_URL + querystring, function(data) {
        $(list_container_name()).html(data);
        connect_listing_click_handler();

        $('li.paginator').on('click', paginate_click);
    });
}


/**
 * Load listings list from saved previous HTML
 */
function load_listings_cached() {
    if (listing_list_cache == null) {
        load_listings();
    } else {
        $(list_container_name()).html(listing_list_cache);
    }

    $('li.paginator').on('click', paginate_click);
}


/**
 * Returns bool whether or not listing detail container is separate from list container.
 */
function is_detail_separate() {
    return $('.listing-info').is(':visible');
}


/**
 * Return the selector name of container for listing detail.
 */
function detail_container_name(is_separate) {
    return is_separate ? '.listing-info' : '.listing-list';
}


function list_container_name() {
    return '.listing-list-container';
}


function display_listing_detail(is_separate, container, url) {
    if (url == null) {
        return;
    }

    container.empty();

    if (! is_separate) {
        container.html(
            '<button class="btn btn-default listing-back"><span class="glyphicon glyphicon-chevron-left"></span> Back</button>'
        );
    }

    $.get(url, function(data) {
        container.append(data);

        // Modal popup on 'contact seller' button click
        container.find('button.create-thread-btn').on('click', function() {
            var url = $(this).attr('form-url') ;

            $('#create-modal').modal();
            $.get(url, function(data) {
                var modal = $('#create-modal');
                modal.find('.modal-body').html(data);

                add_create_form_handler();
            });
        });
    });

    container.find('button.listing-back').on('click', function() {
        selection_url = null;
        $(detail_container_name(true)).empty();
        load_listings_cached();
        $(list_container_name()).find('.listing.selection').removeClass('selection');
        connect_listing_click_handler();
    });
}


function connect_listing_click_handler() {
    var listings = $('.listing-list .listing');

    listings.off('click');
    listings.on('click', listing_selected);
}

$(document).ready(function() {
    $('.add-filter-field').on('click', add_filter_field);
    $('.listing-filter').on('change', filter_changed);
    $(window).on('resize', on_window_resize);

    $('.filter-container button.btn-success').on('click', load_listings);
    $('#filter-modal').find('button.btn-success').on('click', load_listings);
    $('.xs-filter-btn').on('click', xs_filter_click);

    load_listings();
});

$(window).load(function() {
    set_container_heights();
});

