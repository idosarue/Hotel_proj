const log = console.log.bind(console,"calendar.html")

// new date
const date = new Date();
let month = date.getMonth()


// todays date
const nowDate = new Date()
const todayMonth = nowDate.getMonth()
const todayYear = nowDate.getFullYear()


// months names
const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


// week day names
const weekDays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];

// inputs
const checkInInput = $('#check_in_date')
const checkOutInput = $('#check_out_date')

checkInInput.val(date.toLocaleDateString())
checkOutInput.val(new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1).toLocaleDateString())

const displayDateHeaders = (checkIn, checkOut) => {
    $("#check-in-day").text(checkIn.getDate())
    $('#check-out-day').text(checkOut.getDate())
    $("#check-in-month .month-name").text(months[checkIn.getMonth()].substring(0,3).toUpperCase())
    $("#check-in-month .week-day").text(weekDays[checkIn.getDay()].toUpperCase())
    $("#check-out-month .month-name").text(months[checkOut.getMonth()].substring(0,3).toUpperCase())
    $("#check-out-month .week-day").text(weekDays[checkOut.getDay()].toUpperCase())
}

displayDateHeaders(date, new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1))


// dusaply the date range on the calendars

const displayDateRange = () => {
    const x = $(`.calendar .days`).children()
    for (let i =0; i <x.length; i++ ){
        if ($(x[i]).attr('data-date') && $(x[i]).attr('data-date') == new Date(checkInInput.val()).toLocaleDateString()){
            $(x[i]).addClass('selected')
        } else if (new Date($(x[i]).attr('data-date')) <= new Date(checkOutInput.val()) && new Date($(x[i]).attr('data-date')) > new Date(checkInInput.val())) {
            $(x[i]).addClass('selected-check-out')
            log('selected-che')

        }
    }
}



let selectedDates = []

// Create the first cal
const createCal = (calObject, date) => {
    let days = []
    let displayWeekDays = []
    
    // create the weekdays divs
    weekDays.forEach(element => displayWeekDays += `<div class="weekday">${element.toUpperCase()}</div>`)
    
    // get the last day of the month
    const lastDay = new Date(
        date.getFullYear(),
        date.getMonth() + 1,
        0
        ).getDate()
    // get the last weekday of the previous month
    const previousLastDay = new Date(
        date.getFullYear(),
        date.getMonth(),
        0
        ).getDay()


    $(`${calObject}.calendar .month .date h3`).text(`${months[date.getMonth()]} ${date.getFullYear()}`)


    // add empty divs for last months days  
    for (let i = 0; i <= previousLastDay; i++){
        // always start the dates on the first row
        if (previousLastDay <= 5){
            days.push('<div></div>')
        }
    }


    for (let i = 1; i <= lastDay; i++){
        if (i <= nowDate.getDate() && date.getMonth() == todayMonth && date.getFullYear() == todayYear ){
            days.push(`<div class="disabled">${i}</div>`)
        }else {
            days.push(`<div data-date="${date.getMonth() + 1}/${i}/${date.getFullYear()}" class="clickable">${i}</div>`)
        }
    }

    $(`${calObject} .days`).html(days)

    displayDateRange()

    $('.weekdays').html(displayWeekDays)
}

// ***** Increase and decrease months *****

// next month
$('.next').click((e) => {
    date.setMonth(date.getMonth() + 1)
    createCal('.first-calendar', date)
    createCal('.second-calendar', new Date(date.getFullYear(), date.getMonth() + 1))
    $('.prev').removeClass('disabled')
})

// previous month

$('.prev').click((e) => {
    if(date.getFullYear() == todayYear && date.getMonth() - 1 == todayMonth) $('.prev').addClass('disabled')
    if(date.getFullYear() == todayYear && date.getMonth() == todayMonth) return
    date.setMonth(date.getMonth() - 1)
    createCal('.first-calendar', date)
    createCal('.second-calendar', new Date(date.getFullYear(), date.getMonth() + 1))
})


// create the initial calendars
createCal('.first-calendar', date)
createCal('.second-calendar', new Date(date.getFullYear(), date.getMonth() + 1))

// *** add dates to form ****
const validateDateForm = (checkInDate, checkOutDate) => {
    $('.selected-check-out').removeClass('selected-check-out')
    $('.selected').removeClass('selected')
    let checkIn = checkInDate
    let checkOut = checkOutDate

    if(checkOutDate <= checkInDate ) {
        checkOut = new Date(checkInDate.getFullYear(), checkInDate.getMonth(), checkInDate.getDate() + 1)
    }

    checkInInput.val(checkIn.toLocaleDateString())
    checkOutInput.val(checkOut.toLocaleDateString())

    displayDateRange()

    displayDateHeaders(new Date(checkInInput.val()), new Date(checkOutInput.val()))
}

let counter = 0;
$(document).on('click', '[data-date]', (e) => {
    counter++
    let checkInDate
    let checkOutDate

    let checkInInput = $('#check_in_date')
    // alow 2 clicks 
    switch (counter) {
        case 1:
            checkInDate = new Date($(e.target).attr('data-date'))
            validateDateForm(checkInDate, checkInDate)
            break
        case 2:
            checkInDate = new Date(checkInInput.val())
            checkOutDate = new Date($(e.target).attr('data-date'))
            if (checkOutDate <= checkInDate){
                validateDateForm(checkOutDate, checkOutDate)
                counter = 1
                break
            }
            validateDateForm(checkInDate, checkOutDate)
            counter = 0
            break;
    }
})