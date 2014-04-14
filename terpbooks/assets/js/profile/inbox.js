/*
JS functions involving the 'received requests' column of profile page.
 */

/**
 * Connects message selection handler to all received requests in inbox.
 */
function connect_inbox_click_handler() {
    var messages = $('.inbox-list-container .profile-item');

    messages.off('click');
    messages.on('click', message_selected('.inbox-list-container', 'inbox'));
}


/**
 * Ajax load all transaction requests into middle list.
 */
function load_inbox() {
    $.get(INBOX_URL, function(data) {
        var inbox_container = $('.inbox-list-container');
        inbox_container.find('ul').remove();
        inbox_container.append(data);
        connect_inbox_click_handler();
    });
}
