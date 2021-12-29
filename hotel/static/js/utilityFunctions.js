// ***** Functions to control Decrement Buttons *****

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
