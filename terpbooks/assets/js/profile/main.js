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

        container.animate({ scrollTop: container.prop('scrollHeight') }, 500);

        container.find('.thread-container button.inbox-back').on('click', back_message_thread(box));
        container.find('.thread-container form').on('submit', message_form_submit(container_str, box));

        // Connect handlers for marking listings as pending/sold/available
        container.find('.thread-container button.mark-pend-btn').on('click', mark_listing(
            '<p>Marking a listing as pending means that you have come to an ' +
                'agreement with a buyer. This will disable all further messages and requests ' +
                'about this listing. Are you sure you want to do this?</p>',
            'Yes'
        ));

        container.find('.thread-container button.mark-sold-btn').on('click', mark_listing(
            '<p>Are you sure you want to mark this listing as sold?</p>',
            'Yes'
        ));

        container.find('.thread-container button.mark-avail-btn').on('click', mark_listing(
            '<p>Are you sure you want to mark this listing as available again?</p>',
            'Yes'
        ));
    }
}


/**
 * Resizes all columns on profile page to page height - header and banner
 */
function resize_columns() {
    var h = $(window).height() - $('.navbar').height() - $('.banner').height();

    $('.listing-list-container').height(h);
    $('.inbox-list-container').height(h);
    $('.outbox-list-container').height(h);
}


function on_resize_handler() {
    var timeout_id = null;

    return function() {
        if (timeout_id != null) {
            clearTimeout(timeout_id);
        }

        timeout_id = setTimeout(function() {
            resize_columns();
        }, 200);
    }
}


$(document).ready(function() {
    load_listings();
    load_inbox();
    load_outbox();
});

$(window).load(function() {
    resize_columns();
    $(window).on('resize', on_resize_handler());
});
