/*
 JS functions involving the 'sent request' column of profile page.
 */

/**
 * Connects message selection handler to all sent requests in outbox.
 */
function connect_outbox_click_handler() {
    var messages = $('.outbox-list-container .profile-item');

    messages.off('click');
    messages.on('click', message_selected('.outbox-list-container', 'outbox'));
}


function load_outbox() {
    $.get(OUTBOX_URL, function(data) {
        var outbox_container = $('.outbox-list-container');
        outbox_container.find('ul').remove();
        outbox_container.append(data);

        connect_outbox_click_handler();
    });
}