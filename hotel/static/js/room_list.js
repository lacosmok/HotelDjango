$(document).ready(function () {
    url = document.URL.split("/");
    console.log(url[5])
    $.ajax({
        type: "GET",
        url: "/api/hotels/" + url[5] + "/rooms",
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    })
        .done(function (data) {
            rooms = data.rooms;
            console.log("success", rooms);
            html = "";
            for (var i = 0, len = rooms.length; i < len; i++) {
                html +=
                    "<img src=" + rooms[i].photo + " class=\"thumbnail\" width=\"300px\" /></br>" +
                    "Room:" + rooms[i].name + "</br>" +
                    "desc:" + rooms[i].description + "</br>" +
                    "<button type=\"button\" class=\"btn btn-primary book \" data-toggle=\"modal\"" +
                    " data-target=\"#myModal\" data-value= " + rooms[i].pk + "> Book a room </button>"
                document.getElementById("rooms").innerHTML = html;
            }
        })
        .fail(function (data) {
            console.log("error", data);
        })






    $("#reservationForm").submit(function (event) {
        event.preventDefault();
        var csrftoken = $.cookie('csrftoken');
        var data = {
            start_date: $('#start_date').val(),
            end_date: $('#end_date').val(),
            room: parseInt($(this).data('id'), 10),
        };
        $.ajax({
            type: "POST",
            url: "/api/hotels/" + url[5] + "/rooms",
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        })
            .then(function (resp) {
                    console.log('done')
                    return resp
                },
                function (resp) {
                    console.log(resp, "fail")
                })
            .always(function (resp) {
                console.log(resp, "always")

            });
    })

});

