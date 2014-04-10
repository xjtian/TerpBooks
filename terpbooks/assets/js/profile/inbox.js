/*
JS functions involving the 'received requests' column of profile page.
 */

/**
 * Connects message selection handler to all received requests in inbox.
 */
function connect_inbox_click_handler() {
    var messages = $('.inbox-list-container .profile-item');

    messages.off('click');
    messages.on('click', message_selected);
}


function message_selected() {
    var url = $(this).attr('thread-url');

    $.get(url, show_message_thread);
}


/**
 * Takes HTML for transaction thread messages and puts it into the 'Received Requests' column.
 */
function show_message_thread(data) {
    var container = $('.inbox-list-container');
    container.find('ul').remove();
    container.find('.thread-container').remove();
    container.append(data);

    container.find('.thread-container button.inbox-back').on('click', back_message_thread);
    container.find('.thread-container form').on('submit', message_form_submit);
}


/**
 * Click handler for 'back' button on message thread view.
 */
function back_message_thread() {
    $('.inbox-list-container > div.thread-container').remove();

    load_inbox();
}


function message_form_submit() {
    var data = $(this).serialize();
    $.post($(this).attr('action'), data, show_message_thread);

    return false;
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
