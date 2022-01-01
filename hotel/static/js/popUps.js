// Display the room form
let roomContainer = $('.room-container')


$('.guests').click(() => {
    if (roomContainer.css('display') == 'none') return roomContainer.css('display', 'block')
    roomContainer.css('display', 'none')
})

// Hide the form

$(document).click((e) => {
    // check to see if an element has class to avoid errors
    if ($(e.target).attr('class')){
        if (!Array.from($(e.target).parents()).includes(roomContainer[0]) && e.target != roomContainer[0] && e.target != $('.guests')[0] && !($(e.target).attr('class').includes('remove-room'))) {
            roomContainer.css('display', 'none')
        }
    }
})

// Display the login form

let loginContainer = $('#login-container')

$('#login-btn').click(() => {
    if (loginContainer.css('display') == 'none') return loginContainer.css('display', 'flex')
    loginContainer.css('display', 'none')
})

// Hide the login form

$(loginContainer).click((e) => {
    // check to see if an element has an id to avoid errors
    if (e.target.id){
        if(e.target == loginContainer[0] || e.target.id == 'close-btn'){
            loginContainer.css('display', 'none')
        }
    }
})