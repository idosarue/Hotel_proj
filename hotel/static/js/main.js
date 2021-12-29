import {
disableAdultsDecrementButton, 
disableChildrenDecrementButton, 
enableAdultsDecrementButton, 
enableChildrenDecrementButton, 
disableAdultsIncrementButton,
disableChildrenIncrementButton, 
enableAdultsIncrementButton,
enableChildrenIncrementButton,
} from './utilityFunctions.js'


// Room object to append
function createRoom(num){
    let newRoom = 
    `<div class="room flex" id="room${num}">
        <div class="far fa-times-circle remove-room hidden" id="remove-room${num}"></div>
        <p>Room ${num}</p>
        <div class="show-val-adults flex flex-column flex-center">
            <label for="increment-${num}-adults">Adults</label>
            <div class="con flex space-between">
                <input class='adults-input' id='room-${num}-adults' name='room-${num}-adults' type="hidden" value="1">   
                <button class="increment increment-adults" type="button">+</button>
                <span>1</span>
                <button class="decrement decrement-adults disabled" disabled='true' type="button">-</button>
            </div>
        </div>
        <div class="show-val-children flex flex-column flex-center">
            <label for="increment-${num}-children">Children</label>
            <div class="con flex space-between">
                <input class='children-input' id='room-${num}-children' name='room-${num}-children' type="hidden" value="0">
                <button class="increment increment-children" type="button">+</button>
                <span>0</span>
                <button class="decrement decrement-children disabled" disabled='true' type="button">-</button>
            </div>
        </div>
    </div>
    `
    return newRoom
}

// Remove Room Button to append


// Append the initial room
let formSet = $('#form-set')
formSet.append(createRoom(1))
let num = $('.room').length


// Add a room on click
$('#add-more').click(function() {
    num ++
    formSet.append(createRoom(num))
    $('.remove-room').removeClass('hidden')
});



// Increase the value of the childen/adults
$(document).on('click', '.increment', (e) => {
    let form = $(e.target).parent().children('input')
    let span = $(e.target).parent().children('span')
    console.log(form, 'form')
    console.log(e.target, 'targer')
    let currentFormVal = parseInt(form.val())
    currentFormVal += 1
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
    currentFormVal -= 1
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
    for (let i = 0; i < rooms.length; i++){
        $(rooms[i]).children('p').text(`Room ${i + 1}`)
        $(rooms[i]).children('.show-val-adults').children('.con').children('.adults-input').attr('id', `room-${i+1}-adults`).attr('name', `room-${i+1}-adults`)
        $(rooms[i]).children('.show-val-children').children('.con').children('.children-input').attr('id', `room-${i+1}-children`).attr('name', `room-${i+1}-children`)
    }
    num = rooms.length

    if (num == 1) $('.remove-room').addClass('hidden')

})


let roomContainer = $('.room-container')

// Display the form
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
