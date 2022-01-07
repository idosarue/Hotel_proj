// add a border to the inputs on click

// $(document).on('click', '.signup-field', (e) => {
//     $('.signup-field').addClass('bordered-input')
// })

$('.signup-field input').click( (e) => {
    $('.bordered-input').removeClass('bordered-input')
    $(e.target).parent().addClass('bordered-input')
})

$(document).click((e) => {
    if ($(e.target).find($('.signup-field')).length) return $('.signup-field').removeClass('bordered-input')
})

// set the width of label
$('label[for="id_password2"]').css('width', '215px')
$('label[for="id_phone_number"]').css('width', '190px')