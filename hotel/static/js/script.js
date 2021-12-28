import {
disableAdultsDecrementButton, 
disableChildrenDecrementButton, 
enableAdultsDecrementButton, 
enableChildrenDecrementButton, 
disableAdultsIncrementButton,
disableChildrenIncrementButton, 
enableAdultsIncrementButton,
enableChildrenIncrementButton
} from './utilityFunctions.js'


function createRoom(num){
    let newRoom = `
    <div class="room" id="room${num}">
    <p>Room ${num}</p>
    <div class="show-val-adults">
        <label for="increment-${num}-adults">Adults</label>
        <div class="con">
            <input class='adults-input' id='room-${num}-adults' name='room-${num}-adults' type="hidden" value="1">
            <button class="increment increment-adults" type="button">+</button>
            <span ">1</span>
            <button class="decrement decrement-adults" type="button">-</button>
        </div>
    </div>
    <div class="show-val-children">
        <label for="increment-${num}-children">Children</label>
        <div class="con"> 
            <input class='children-input' id='room-${num}-children' name='room-${num}-children' type="hidden" value="0">
            <button class="increment increment-children" type="button">+</button>
            <span>0</span>
            <button class="decrement decrement-children" type="button">-</button>
        </div>
    </div>
    <button class='remove-room' id="remove-room${num}" type="button">Remove Room</button>
    </div>`

    return newRoom
}






let formSet = $('#form-set')

formSet.append(createRoom(1))

let adultSpans = $('.show-val-adults span')
let childSpans = $('.show-val-children span')


disableAdultsDecrementButton(adultSpans)
disableChildrenDecrementButton(childSpans)

let num = $('.room').length
$('#add-more').click(function() {
    num ++
    formSet.append(createRoom(num))
    adultSpans = $('.show-val-adults span')
    childSpans = $('.show-val-children span')
    disableAdultsDecrementButton(adultSpans)
    disableChildrenDecrementButton(childSpans)
});





$(document).on('click', '.increment', (e) => {
    let adultSpans = $('.show-val-adults span')
    let childSpans = $('.show-val-children span')
    console.log(adultSpans, 'adults')
    console.log(childSpans, 'children')
    let form = $(e.target).parent().children('input')
    let span = $(e.target).parent().children('span')
    let currentFormVal = parseInt(form.val())
    currentFormVal += 1
    console.log(span)
    form.val(currentFormVal)
    span.text(currentFormVal)
    disableAdultsDecrementButton(adultSpans)
    disableChildrenDecrementButton(childSpans)
    enableAdultsDecrementButton(adultSpans)
    enableChildrenDecrementButton(childSpans)
    disableAdultsIncrementButton(adultSpans)
    disableChildrenIncrementButton(childSpans)
    enableAdultsIncrementButton(adultSpans)
    enableChildrenIncrementButton(childSpans)
})

$(document).on('click', '.decrement', (e) => {
    let form = $(e.target).parent().children('input')
    let span = $(e.target).parent().children('span')
    let currentFormVal = parseInt(form.val())
    let adultSpans = $('.show-val-adults span')
    let childSpans = $('.show-val-children span')
    currentFormVal -= 1
    form.val(currentFormVal)
    span.text(currentFormVal)
    disableAdultsDecrementButton(adultSpans)
    disableChildrenDecrementButton(childSpans)
    enableAdultsDecrementButton(adultSpans)
    disableAdultsIncrementButton(adultSpans)
    disableChildrenIncrementButton(childSpans)
    enableAdultsIncrementButton(adultSpans)
    enableChildrenIncrementButton(childSpans)
})


$(document).on('click', '.remove-room', (e) => {
    if ($('.room').length == 1) return
    $(e.target).parent().remove()
    let rooms = $('.room')
    for (let i = 0; i < rooms.length; i++){
        $(rooms[i]).children('p').text(`Room ${i + 1}`)
        // $(rooms[i]).children('.show-val-children').children('.con').children('span').attr('id', `room-${i+1}-children-val`)
        // $(rooms[i]).children('.show-val-adults').children('.con').children('span').attr('id', `room-${i+1}-adults-val`)
        $(rooms[i]).children('.show-val-adults').children('.con').children('.adults-input').attr('id', `room-${i+1}-adults`).attr('name', `room-${i+1}-adults`)
        $(rooms[i]).children('.show-val-children').children('.con').children('.children-input').attr('id', `room-${i+1}-children`).attr('name', `room-${i+1}-children`)
        // $(rooms[i]).children('.show-val-adults').children('.con').children('.decrement-adults').attr('id', `decrement-room-${i+1}-adults`)
    }

    num = rooms.length
})
