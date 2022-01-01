import {
disableAdultsDecrementButton, 
disableChildrenDecrementButton, 
enableAdultsDecrementButton, 
enableChildrenDecrementButton, 
disableAdultsIncrementButton,
disableChildrenIncrementButton, 
enableAdultsIncrementButton,
enableChildrenIncrementButton,
createRoom,
} from './utilityFunctions.js'


// Room object to append


// Global variables
let num = $('.room').length
let roomNum = parseInt($('#room-counter').text().match(/\d/g))
let guestsCounter = $('#guests-counter') 
let roomsCounter = $('#room-counter') 
let formSet = $('#form-set')

// Append the initial room
formSet.append(createRoom(1))


// Add a room on click
$('#add-more').click(function() {
    let guestsNum = parseInt(guestsCounter.text().match(/\d/g))
    roomNum++
    guestsNum++
    roomsCounter.text(`${roomNum} Rooms`)
    guestsCounter.text(`${guestsNum} Guests`)
    formSet.append(createRoom(roomNum))
    $('.remove-room').removeClass('hidden')
});



// Increase the value of the childen/adults
$(document).on('click', '.increment', (e) => {
    let form = $(e.target).parent().children('input')
    let span = $(e.target).parent().children('span')
    let currentFormVal = parseInt(form.val())
    currentFormVal += 1
    let guestsNum = parseInt($('#guests-counter').text().match(/\d/g))
    guestsNum++
    guestsCounter.text(`${guestsNum} Guests`)
    form.val(currentFormVal)
    span.text(currentFormVal)
    let adultSpans = $('.show-val-adults.flex-column.flex-center span')
    let childSpans = $('.show-val-children.flex-column.flex-center span')
    enableAdultsDecrementButton(adultSpans)
    enableChildrenDecrementButton(childSpans)
    disableAdultsIncrementButton(adultSpans)
    disableChildrenIncrementButton(childSpans)
    enableAdultsIncrementButton(adultSpans)
    enableChildrenIncrementButton(childSpans)
})

// Decrease the value of the childen/adults
$(document).on('click', '.decrement', (e) => {
    let form = $(e.target).parent().children('input')
    let span = $(e.target).parent().children('span')
    let currentFormVal = parseInt(form.val())
    let guestsNum = parseInt($('#guests-counter').text().match(/\d/g))
    currentFormVal -= 1
    guestsNum--
    guestsCounter.text(`${guestsNum} Guests`)
    form.val(currentFormVal)
    span.text(currentFormVal)
    let adultSpans = $('.show-val-adults.flex-column.flex-center span')
    let childSpans = $('.show-val-children.flex-column.flex-center span')
    disableAdultsDecrementButton(adultSpans)
    disableChildrenDecrementButton(childSpans)
    enableAdultsDecrementButton(adultSpans)
    enableAdultsIncrementButton(adultSpans)
    enableChildrenIncrementButton(childSpans)
})

// Remove a room
$(document).on('click', '.remove-room', (e) => {
    if ($('.room').length == 1) return 
    $(e.target).parent().remove()
    let rooms = $('.room')
    let vals = 0
    for (let i = 0; i < rooms.length; i++){
        $(rooms[i]).children('p').text(`Room ${i + 1}`)
        vals += parseInt($(rooms[i]).children('.show-val-adults').children('.con').children('.adults-input').val())
        vals += parseInt($(rooms[i]).children('.show-val-children').children('.con').children('.children-input').val())
        $(rooms[i]).children('.show-val-adults').children('.con').children('.adults-input').attr('id', `room-${i+1}-adults`).attr('name', `room-${i+1}-adults`)
        $(rooms[i]).children('.show-val-children').children('.con').children('.children-input').attr('id', `room-${i+1}-children`).attr('name', `room-${i+1}-children`)
    }
    
    num = rooms.length
    roomNum--
    roomsCounter.text(`${roomNum} Rooms`)
    guestsCounter.text(`${vals} Guests`)
    if (num == 1) $('.remove-room').addClass('hidden')
})





// Display the form
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