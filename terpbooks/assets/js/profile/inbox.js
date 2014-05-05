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

    messages = $('.tab-content > #inbox .profile-item');

    messages.off('click');
    messages.on('click', message_selected('.tab-content > #inbox', 'inbox'));
}


/**
 * Ajax load all transaction requests into middle list.
 */
function load_inbox() {
    $.get(INBOX_URL, function(data) {
        var inbox_containers = $('.inbox-list-container, .tab-content > #inbox');

        inbox_containers.find('ul').remove();
        inbox_containers.find('.thread-container').remove();
        inbox_containers.append(data);
        connect_inbox_click_handler();
    });
}


function mark_listing(message, confirm) {
    return function() {
        var url = $(this).attr('data-url');

        var modal = $('#edit-modal');
        modal.modal();

        var modal_body = modal.find('.modal-body');
        modal_body.html('<p class="strong">' + message + '</p>');
        modal_body.append(
            '<button class="btn btn-danger confirm-delete-btn">' + confirm + '</button>' +
            '<button class="btn btn-default" data-dismiss="modal">No</button>'
        );

        modal_body.find('button.confirm-delete-btn').on('click', function() {
            $.post(url, {
                csrfmiddlewaretoken: CSRF
            }, function(data) {
                modal_body.html(data);
                load_inbox();
            });
        });
    };
}
