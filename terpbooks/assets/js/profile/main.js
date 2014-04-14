function message_form_submit(container, box) {
    return function() {
        var data = $(this).serialize();
        $.post($(this).attr('action'), data, show_message_thread(container, box));

        return false;
    }
}


/**
 * Click handler for 'back' button on message thread view.
 *
 * box parameter is either 'inbox' or 'outbox'
 */
function back_message_thread(box) {
    return function() {
        $(this).parent().remove();

        if (box == 'inbox') {
            load_inbox();
        } else if (box == 'outbox') {
            load_outbox();
        }
    }
}


function message_selected(container, box) {
    return function() {
        var url = $(this).attr('thread-url');

        $.get(url, show_message_thread(container, box));
    }
}


/**
 * Takes HTML for transaction thread messages and puts it into the container
 * specified by the passed selector string.
 *
 * box parameter is either 'inbox' or 'outbox'
 */
function show_message_thread(container_str, box) {
    return function(data) {
        var container = $(container_str);

        container.find('ul').remove();
        container.find('.thread-container').remove();
        container.append(data);

        container.find('.thread-container button.inbox-back').on('click', back_message_thread(box));
        container.find('.thread-container form').on('submit', message_form_submit(container_str, box));
    }
}

$(document).ready(function() {
    load_listings();
    load_inbox();
    load_outbox();
});
