const date = new Date();
let month = date.getMonth()

const nowDate = new Date()

const todayMonth = nowDate.getMonth()
const todayYear = nowDate.getFullYear()

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

const weekDays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];


// Create the first cal
const createFirstCal = () => {
    let days = ""
    let displayWeekDays = ''
    
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


    $('.calendar .month .date h3').text(`${months[date.getMonth()]} ${date.getFullYear()}`)


    // add empty divs for last months days  
    for (let i = 0; i <= previousLastDay; i++){
        // always start the dates on the first row
        if (previousLastDay <= 5){
            days += '<div></div>'
        }
    }


    for (let i = 1; i <= lastDay; i++){
        
        if (i <= nowDate.getDate() && date.getMonth() == todayMonth && date.getFullYear() == todayYear ){
            days += `<div data-date="${date.getMonth() + 1}/${i}/${date.getFullYear()}" class="disabled">${i}</div>`
        }else {
            days += `<div data-date="${date.getMonth() + 1}/${i}/${date.getFullYear()}" class="clickable">${i}</div>`
        }
    }

    $('.calendar .days').html(days)
    $('.weekdays').html(displayWeekDays)
}

// Create the second cal
const createSecondCal = () => {
    const secondDate = new Date(date.getFullYear(), date.getMonth() + 1)
    let days = ""

    // get the last day of the month
    const lastDay = new Date(
        secondDate.getFullYear(),
        secondDate.getMonth() + 1,
        0
    ).getDate();

    // get the last weekday of the previous month
    const previousLastDay = new Date(
        secondDate.getFullYear(),
        secondDate.getMonth(),
        0
        ).getDay()

    // add empty divs for last months days 
    for (let i = 0; i <= previousLastDay; i++){
        // always start the dates on the first row
        if (previousLastDay <= 5){
            days += '<div></div>'
        }
    }


    $('.second-calendar .month .date h3').text(`${months[secondDate.getMonth()]} ${secondDate.getFullYear()}`)


    for (let i = 1; i <= lastDay; i++){
        days += `<div data-date="${secondDate.getMonth() + 1}/${i}/${date.getFullYear()}" class="clickable">${i}</div>`
    }
  
    
    $('.second-calendar .days').html(days)
    
}


// ***** Increase and decrease months *****

// next month
$('.next').click((e) => {
    date.setMonth(date.getMonth() + 1)
    createFirstCal()
    createSecondCal()
    $('.prev').removeClass('disabled')
})

// previous month

$('.prev').click((e) => {
    if(date.getFullYear() == todayYear && date.getMonth() - 1 == todayMonth) $('.prev').addClass('disabled')
    if(date.getFullYear() == todayYear && date.getMonth() == todayMonth) return
    date.setMonth(date.getMonth() - 1)
    createFirstCal()
    createSecondCal()     
})


// first calendar
createFirstCal()

// scond calendar
createSecondCal()


// add dates to form
const validateDateForm = () => {
    const checkInDate = new Date($('#check_in_date').val())
    const checkOutDate = new Date($('#check_out_date').val())
    if(checkOutDate <= checkInDate ) {
        $('#check_in_date').val(checkInDate.toLocaleDateString())
        $('#check_out_date').val(new Date(checkInDate.setDate(checkInDate.getDate() + 1)).toLocaleDateString())
        return
    }
    $('#check_in_date').val(checkInDate.toLocaleDateString())
    $('#check_out_date').val(checkOutDate.toLocaleDateString())
}

let counter = 0;
$(document).on('click', '.clickable', (e) => {
    console.log('clikc')
    counter++
    // alow 2 clicks 
    if (counter == 3){
        $('.selected').removeClass('selected')
        $('.selected-check-out').removeClass('selected-check-out')
        counter = 1
    }  

       
    // for the first time a date is clicked the check out and check in will the same, so check out will be equel to the checkin + 1
    
    if (counter == 1) {
        $('#check_in_date').val($(e.target).attr('data-date'))        
        $(e.target).addClass('selected')
    }

    if (counter == 2){
        $(e.target).addClass('selected-check-out')
    }

    // In the second time the value for the checkout is already stored in the check_in_date input, so we just get the value and pass in the new date that was clicked
    $('#check_out_date').val($(e.target).attr('data-date'))
    validateDateForm($('#check_in_date').val(), $(e.target).attr('data-date'))
})