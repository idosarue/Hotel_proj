// ***** Functions to control Decrement Buttons *****

//  create the room object
export function createRoom(num){
    let newRoom = 
    `<div class="room flex" id="room${num}">
        <div class="far fa-times-circle remove-room hidden clickable" id="remove-room${num}"></div>
        <p>Room ${num}</p>
        <div class="show-val-adults flex flex-column flex-center">
            <label for="increment-${num}-adults">Adults</label>
            <div class="con flex space-between">
                <input class='adults-input' id='room-${num}-adults' name='room-${num}-adults' type="hidden" value="1">   
                <button class="increment increment-adults far fa-times-circle rotate" type="button"></button>
                <span>1</span>
                <button class="decrement decrement-adults disabled fal fa-minus-circle" disabled='true' type="button"></button>
            </div>
        </div>
        <div class="show-val-children flex flex-column flex-center">
            <label for="increment-${num}-children">Children</label>
            <div class="con flex space-between">
                <input class='children-input' id='room-${num}-children' name='room-${num}-children' type="hidden" value="0">
                <button class="increment increment-children far fa-times-circle rotate" type="button"></button>
                <span>0</span>
                <button class="decrement decrement-children disabled fal fa-minus-circle" disabled='true' type="button"></button>
            </div>
        </div>
    </div>
    `
    return newRoom
}


// disable decrement if value is 1
export function disableAdultsDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() == 1){
            console.log($('.decrement-adults')[i], 'obg')
            $($('.decrement-adults')[i]).prop('disabled', true)
            $($('.decrement-adults')[i]).addClass('disabled')
        }
    }
}

// disable decrement if value is 0
export function disableChildrenDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() == 0){
            $($('.decrement-children')[i]).prop('disabled', true)
            $($('.decrement-children')[i]).addClass('disabled')
        }
    }
}

// Enable decrement if value is bigger than 1
export function enableAdultsDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() > 1){
            $($('.decrement-adults')[i]).prop('disabled', false)
            $($('.decrement-adults')[i]).removeClass('disabled')
        }
    }
}

// Enable decrement if value is bigger or equal to 1
export function enableChildrenDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() >= 1){
            $($('.decrement-children')[i]).prop('disabled', false)
            $($('.decrement-children')[i]).removeClass('disabled')
        }
    }
}


// Functions to control Increment Buttons

// disable incerment button if value is 3
export function disableAdultsIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() > 2){
            $($('.increment-adults')[i]).prop('disabled', true)
            $($('.increment-adults')[i]).addClass('disabled')
        }
    }
}

// disable incerment button if value is 2
export function disableChildrenIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() == 2){
            $($('.increment-children')[i]).prop('disabled', true)
            $($('.increment-children')[i]).addClass('disabled')

        }
    }
}

// enable incerment button if value is less than 3
export function enableAdultsIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() < 3){
            $($('.increment-adults')[i]).prop('disabled', false)
            $($('.increment-adults')[i]).removeClass('disabled')

        }
    }
}

// enable incerment button if value is 1
export function enableChildrenIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() < 2){
            $($('.increment-children')[i]).prop('disabled', false)
            $($('.increment-children')[i]).removeClass('disabled')
        }
    }
}


// Create the adult and child spans variables for value check 

export function giveSpans(){
    let adultSpans = $('.show-val-adults.flex-column.flex-center span')
    let childSpans = $('.show-val-children.flex-column.flex-center span')

    return {adultSpans: adultSpans, childSpans: childSpans}
}



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
