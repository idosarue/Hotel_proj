let num = 1
$('#add_more').click(function() {
    num ++
    let newRoom = `
    <div id="room">
    <input id='room-${num}-adults' name='room-${num}-adults' type="number" value="1">
    <input id='room-${num}-children' name='room-${num}-children' type="number" value="0">
    <label for="increment-${num}-adults">Adults</label>
    <button class="increment" id="increment-${num}-adults" type="button">+</button>
    <label for="increment-${num}-children">Children</label>
    <button class="increment" id="increment-${num}-children" type="button">+</button>
    </div>`
    let formSet = $('#form_set')
    formSet.append(newRoom)    
});


$(document).on('click', '.increment', (e) => {
    formId = $(`#${e.target.id.replace('increment', 'room')}`)
    currentFormVal = parseInt(formId.val())
    formId.val(currentFormVal + 1)
    console.log(currentFormVal)
})

    