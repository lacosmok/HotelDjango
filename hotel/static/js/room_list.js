$(document).ready(function () {
    var url = document.URL.split("/");
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
            var html = "";
            for (var i = 0; i < rooms.length; i++) {
                html +=
                    "<div class='col-sm-6'><div class='well margin'>" +
                    "<img src=" + rooms[i].photo + " class=\"thumbnail\" width=\"300px\" /></br>" +
                    "Room:" + rooms[i].name + "</br>" +
                    "desc:" + rooms[i].description + "</br>" +
                    "<button type=\"button\" class=\"btn btn-primary book \" data-toggle=\"modal\"" +
                    " data-target=\"#myModal\" data-id=' " + rooms[i].pk + "'> Book a room </button></div></div>"
                document.getElementById("rooms").innerHTML = html;
            }
        })
        .fail(function (data) {
            console.log("error", data);
        })


    $("#reservationForm").submit(function (event) {
        event.preventDefault();
        var csrftoken = $.cookie('csrftoken');
        var room = $(".book").data('id');
        var data = {
            start_date: this['start_date'].value,
            end_date: this['end_date'].value,
            room: parseInt(room, 10)
        };
        console.log(data.room);
        $.ajax({
            type: "POST",
            url: "/api/hotels/" + url[5] + "/rooms/",
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        })
            .then(function (resp) {
                    console.log('done')
                    window.location.replace("/drf/profile/")
                    return resp
                },
                function (resp) {
                    var html = "";
                    html += "<div class=\"alert alert-danger\" role=\"alert\" >" +
                        resp.responseText + "</div>"
                    document.getElementById("errors").innerHTML = html;
                    return (resp)
                })
            .always(function (resp) {
                console.log(resp, "always")

            });
    })

});

