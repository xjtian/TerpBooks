/**
 * Event handler for add author form button click.
 * Fetches the formset with one more field than currently via AJAX,
 * while maintaining the data already entered.
 */
function add_author_form() {
    var data = $('.author-formset-container').find('input').serialize();
    data = $.param({'csrfmiddlewaretoken': CSRF}) + '&' + data;

    $.post(FORMSET_URL, data, function(data) {
        $('.author-formset-container').html(data);
        $('.add-formset-field').on('click', add_author_form);
    });
}

$(document).ready(function() {
    $('.add-formset-field').on('click', add_author_form);
});