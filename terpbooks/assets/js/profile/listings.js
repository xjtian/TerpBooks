/*
JS functions involving the 'Your Listings' column of profile page.
 */

function add_edit_form_handler() {
    $('#edit-modal').find('form').on('submit', edit_form_submitted);
}


function edit_form_submitted() {
    var data = $(this).serialize();
    $.post($(this).attr('action'), data, function(data) {
        $('#edit-modal').find('.modal-body').html(data);
        add_edit_form_handler();
        load_listings();
    });

    return false;
}


/**
 * Connect the click handler to all listings under 'Your Listings'
 */
function connect_listing_click_handler() {
    var listings = $('.listing-list-container .profile-item');

    listings.off('click');
    listings.on('click', listing_selected);
}


/**
 * Click handler for selection of a listing.
 *
 * Pops up a modal with a bound form to edit the listing.
 */
function listing_selected() {
    var url = $(this).attr('form-url');

    $('#edit-modal').modal();
    $.get(url, function(data) {
        var modal = $('#edit-modal');
        modal.find('.modal-body').html(data);
        add_edit_form_handler();
    });
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
