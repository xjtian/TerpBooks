function add_form_handler() {
    $('#edit-modal').find('form').on('submit', form_submitted);
}


function listing_selected() {
    var url = $(this).attr('form-url');

    $('#edit-modal').modal();
    $.get(url, function(data) {
        var modal = $('#edit-modal');
        modal.find('.modal-body').html(data);
        add_form_handler();
    });
}


function form_submitted() {
    var data = $(this).serialize();
    $.post($(this).attr('action'), data, function(data) {
        $('#edit-modal').find('.modal-body').html(data);
        add_form_handler();
        load_listings();
    });

    return false;
}


function connect_listing_click_handler() {
    var listings = $('.listing-list-container .listing');

    listings.off('click');
    listings.on('click', listing_selected);
}


/**
 * Ajax load all listings belonging to current user into left list.
 */
function load_listings() {
    $.get(YOUR_LISTINGS_URL, function(data) {
        var listings_container = $('.listing-list-container');
        listings_container.find('ul').remove();
        listings_container.append(data);
        connect_listing_click_handler();
    });
}


$(document).ready(function() {
    load_listings();
});