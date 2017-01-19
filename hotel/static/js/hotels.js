/**
 * Created by pc on 18.01.17.
 */

$(document).ready(function () {
    var hotels = []
    $.ajax({
        type: "GET",
        url: "/api/",
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    })
        .done(function (data) {
            hotels = data.hotels
            console.log("success", hotels[0]);
            html = "";
            for (var i = 0, len = hotels.length; i < len; i++) {
                html +=
                    "<img src=" + hotels[i].photo + " class=\"thumbnail\" width=\"300px\" /></br>" +
                    "Hotel:" + hotels[i].name + "</br>" +
                    "desc:" + hotels[i].description + "</br>" +
                    "<a href='/drf/hotels/"+ hotels[i].pk + "/rooms/' " +
                    " class=\"btn btn-default\" role=\"button\">Rooms</a>"
                document.getElementById("hotels").innerHTML = html;
            }
            console.log(html)
        })
        .fail(function (data) {
            console.log("error", data);
        })

});

$("#target").click(function () {
    $.ajax({
        type: "GET",
        url: "/api/",
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    })
});
