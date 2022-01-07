// Display the room form

const calLog = console.log.bind(console, "popups")

let roomContainer = $('.room-container')


$('.guests').click((e) => {

    if (roomContainer.css('display') == 'none') return roomContainer.css('display', 'block')
    roomContainer.css('display', 'none')
})

// Hide the form

$(document).click((e) => {
    try {
        if (!$(e.target).attr('class').split(' ').includes('remove-room') && e.target == $('#room-close')[0]  ){
            roomContainer.css('display', 'none')
        }
    }catch (e) {
        if (e.target == document) {
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
    if ($(e.target).attr('class')){
        if(e.target == loginContainer[0] || $(e.target).attr('class') == 'fas fa-times close-btn flex'){
            loginContainer.css('display', 'none')
        }
    }
})



$(document).click((e) => {
    const calendarPopUp = $('.calendar-popup')
    const target = e.target
    // calLog(calendarPopUp.find($(target)))
    if (e.target == $('#date-overlay')[0]){
        if (calendarPopUp.css('display') == 'none') return calendarPopUp.css('display', 'block')
        calendarPopUp.css('display', 'none')
    }else if (calendarPopUp.find($(target)).length == 0 || $(e.target).attr('class') == 'fas fa-times close-btn flex'){
        calendarPopUp.css('display', 'none')
    }

    
})