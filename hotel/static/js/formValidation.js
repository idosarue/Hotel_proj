$(document).ready( () => {
    $('#delete-button').click( (e) => {
        $target = $(e.target)
        const id = $target.attr('data-id')
        if (confirm('Are you sure you want to delete this post?')){
            $.ajax({
                type: 'DELETE',
                url: '/deletePost/' + id,
                success : (response) => {
                    window.location.href = '/'
                },
                error : (err) => {
                    console.log(err, 'eror')
                }
            })
        }

    })
})

// $("#bookingSearchForm").submit(function (e) {
//     // preventing from page reload and default actions
//     e.preventDefault();
//     // serialize the data for sending the form data.
//     // make POST ajax call
//     var serializedData = $(this).serialize();

//     $.ajax({
//         type: 'GET',
//         url: $(this).attr('action'),
//         data: serializedData,
//         success: function (response) {
//             // on successfull creating object
//             // 1. clear the form.
//             $(this).trigger('reset');
//             window.location = '/rooms?' + serializedData
//             console.log(serializedData)
//             console.log('serializedData')

//             // 2. focus to nickname input 
//             // location.reload(true)
//             // display the newly friend to table.
//         },
//         error: function (response) {
//             // alert the error if any error occured
//             var x = Object.values(response.responseJSON.error)[0][0]
//             console.log(x)
//             $('#result').html(`<div class="alert alert-danger" role="alert"> ${x} </div>`);
//         }
//     })
// });
