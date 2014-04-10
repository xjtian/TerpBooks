function add_form_handler() {
    $('#edit-modal').find('form').on('submit', form_submitted);
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
    var listings = $('.listing-list-container .profile-item');

    listings.off('click');
    listings.on('click', listing_selected);
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


function connect_inbox_click_handler() {
    var messages = $('.inbox-list-container .inbox-request');

    messages.off('click');
    messages.on('click', message_selected);
}


function message_selected() {
    console.log('MOCK');
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

/**
 * Ajax load all transaction requests into middle list.
 */
function load_inbox() {
    $.get(INBOX_URL, function(data) {
        var inbox_container = $('.inbox-list-container');
        inbox_container.find('ul').remove();
        inbox_container.append(data);

    });
}


$(document).ready(function() {
    load_listings();
    load_inbox();
});