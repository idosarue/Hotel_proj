$('#add_more').click(function() {
// var form_idx = $('#id_form-TOTAL_FORMS').val();

// $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
// $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    let formSet = $('#form_set')
    let room = $('#room').html().replace()
    let currentNum = parseInt(room.match(/\d/g))
    console.log(currentNum)
    let newRoom = room.replace(currentNum, currentNum + 1)
    console.log(newRoom)
    formSet.append(newRoom)
});


$('.increment').click(function(e) {
    formId = $(`#${e.target.id.replace('increment', 'room')}`)
    currentFormVal = parseInt(formId.val())
    formId.val(currentFormVal + 1)
    console.log(currentFormVal)
});
    