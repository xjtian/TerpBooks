function listing_selected() {
    console.log('MOCK');
}

function connect_listing_click_handler() {
    var listings = $('.listing-list-container .listing');

    listings.off('click');
    listings.on('click', listing_selected);
}

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