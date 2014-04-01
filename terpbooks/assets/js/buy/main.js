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
function scroll_wrapper_window_resize() {
    if (timeoutID != null) {
        clearTimeout(timeoutID);
    }

    timeoutID = setTimeout(set_scroll_wrapper_height, 200);
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
            filter_wrapper.find('.semester-select').remove();
            filter_wrapper.css('width', '');
            break;
        case 'title':
        case 'isbn':
        case 'class':
        case 'prof':
            if (filter_wrapper.find('input').length != 0) {
                break;
            }

            filter_wrapper.find('.semester-select').remove();
            filter_wrapper.width(300);
            filter_wrapper.append('<input type="text" class="form-control filter-input" />');
            break;
        case 'semester':
            if (filter_wrapper.find('select').length > 1) {
                break;
            }

            $.get(SEMESTER_URL, function(data) {
                var name_map = {};
                $.ajax({
                    url: SEMESTER_LOOKUP_URL,
                    async: false,
                    success: function(data) {
                        name_map = data;
                    }
                });

                filter_wrapper.find('input').remove();
                filter_wrapper.width(300);
                filter_wrapper.append('<select class="form-control semester-select"></select>');

                for (var i = 0; i < data.length; i++) {
                    var sem_val = data[i].semester + ' ' + data[i].year;
                    var sem_str = name_map.forward[data[i].semester] + ' ' + data[i].year;

                    var s = filter_wrapper.find('.semester-select');
                    s.append(new Option(sem_str, sem_val));
                }
            });
            break;
    }
}

/**
 * Event handler for selection of a listing from the list.
 */
function listing_selected() {
    var is_separate = is_detail_separate();
    var url = $(this).attr('detail-url');

    if (is_separate) {
        $('.listing-list .listing.selection').removeClass('selection');
        $(this).addClass('selection');
    }

    display_listing_detail(is_separate, $(detail_container_name(is_separate)), url);
}

/**
 * Event handler for click on add filter field button.
 */
function add_filter_field() {
    $('.listing-filter-wrapper').append(
        '<div class="listing-filter-group">' +
            '<select class="form-control listing-filter">' +
            '<option value="all">All Books</option>' +
            '<option value="title">Title</option>' +
            '<option value="isbn">ISBN</option>' +
            '<option value="class">Class Code</option>' +
            '<option value="semester">Semester</option>' +
            '<option value="prof">Professor</option>' +
            '</select>' +
            '</div>'
    );

    var lf = $('.listing-filter');
    lf.off('change');
    lf.on('change', filter_changed);
}

/*************************
 *
 * End Event Handlers
 *
 *************************/

// </editor-fold>

/**
 * Set listing list container height to fix exactly window minus nav and banner.
 */
function set_scroll_wrapper_height() {
    // Window height - navbar height - banner height - filter bar height
    var h = $(window).height() - $('.navbar').height() - $('.banner').height() - $('.filter-container').outerHeight();

    list_container_name().height(h);
}


/**
 * Populate listings list via ajax call.
 */
function load_listings() {
    $.get(LISTING_LIST_URL, function(data) {
        $(list_container_name()).html(data);
        $('.listing-list .listing').on('click', listing_selected);
    });
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
    if (! is_separate) {
        container.empty();
        container.append(
            '<button class="btn btn-default listing-back"><span class="glyphicon glyphicon-chevron-left"></span> Back</button>'
        );
    }

    $.get(url, function(data) {
        container.append(data);
    });

    if (! is_separate) {
        container.find('button.listing-back').on('click', function() {
            load_listings();
            $('.listing-list .listing').on('click', listing_selected);
        });
    }
}


$(document).ready(function() {
    // TODO: sorting listings
    // TODO: filtering listings logic
    // TODO: pagination front-end
    $('.add-filter-field').on('click', add_filter_field);
    $('.listing-filter').on('change', filter_changed);
    $(window).on('resize', scroll_wrapper_window_resize);

    load_listings();
});

$(window).load(function() {
    set_scroll_wrapper_height();
});

