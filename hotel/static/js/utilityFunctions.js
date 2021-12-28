// ***** Functions to control Decrement Buttons *****

// disable decrement if value is 1
export function disableAdultsDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        console.log($(elements[i]).text())
        if ($(elements[i]).text() == 1){
            $($('.decrement-adults')[i]).prop('disabled', true)

        }
    }
}

// disable decrement if value is 0
export function disableChildrenDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() == 0){
            $($('.decrement-children')[i]).prop('disabled', true)
        }
    }
}

// Enable decrement if value is bigger than 1
export function enableAdultsDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() > 1){
            $($('.decrement-adults')[i]).prop('disabled', false)
        }
    }
}

// Enable decrement if value is bigger or equal to 1
export function enableChildrenDecrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() >= 1){
            $($('.decrement-children')[i]).prop('disabled', false)
        }
    }
}


// Functions to control Increment Buttons

// disable incerment button if value is 3
export function disableAdultsIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() > 2){
            $($('.increment-adults')[i]).prop('disabled', true)
        }
    }
}

// disable incerment button if value is 2
export function disableChildrenIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() == 2){
            $($('.increment-children')[i]).prop('disabled', true)
        }
    }
}

// enable incerment button if value is less than 3
export function enableAdultsIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() < 3){
            $($('.increment-adults')[i]).prop('disabled', false)
        }
    }
}

// enable incerment button if value is 1
export function enableChildrenIncrementButton(elements){
    for (let i = 0; i < elements.length; i++){
        if ($(elements[i]).text() < 2){
            $($('.increment-children')[i]).prop('disabled', false)
        }
    }
}


