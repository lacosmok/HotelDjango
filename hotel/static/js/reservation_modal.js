$("#reservationForm").submit(function (event) {
    event.preventDefault();
    var csrftoken = $.cookie('csrftoken');
    var data = {
        start_date: $('#start_date').val(),
        end_date: $('#end_date').val(),
        room: parseInt($('#room').val(), 10)
    };
    $.ajax({
        type: "POST",
        url:   "/api/hotels/1/rooms/",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
        .then(function(resp){
            console.log('done')
            return resp
        },
            function (resp) {
            console.log(resp, "fail")
        })
        .always(function (resp) {
            console.log(resp, "always")

        });
});