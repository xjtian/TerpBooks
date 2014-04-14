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

        var url = modal.find('.delete-submit').attr('data-url');
        modal.find('.delete-submit').on('click', delete_listing_first(url));
    });
}


function delete_listing_first(url) {
    return function() {
        var body = $('#edit-modal').find('.modal-body');
        body.html(
            '<p class="strong">This will delete the listing permanently and all associated requests. ' +
            'Are you sure you want to do this?</p>' +
            '<button class="btn btn-danger confirm-delete-btn">Yes, delete this listing.</button>' +
            '<button class="btn btn-default" data-dismiss="modal">No, take me away from here!</button>'
        );

        body.find('button.confirm-delete-btn').on('click', function() {
            $.post(url, {
                'csrfmiddlewaretoken': CSRF
            }, function(data) {
                body.html(data);
                load_listings();
            });
        });
    }
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
