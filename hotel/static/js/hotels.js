/**
 * Created by pc on 18.01.17.
 */

$(document).ready(function () {
    var hotels = [];
    $.ajax({
        type: "GET",
        url: "/api/",
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    })
        .done(function (data) {
            hotels = data.hotels;
            var html = "";
            for (var i = 0; i < hotels.length; i++) {
                html +=
                    "<div class='col-sm-6'><div class='well margin'>" +
                    "<img src=" + hotels[i].photo + " class=\"img-thumbnail\" /></br>" +
                    "<p>Hotel:" + hotels[i].name + "</br>" +
                    "desc:" + hotels[i].description + "</br></p>" +
                    "<a href='/drf/hotels/" + hotels[i].pk + "/rooms/' " +
                    " class=\"btn btn-default\" role=\"button\">Rooms</a></div></div>";
                document.getElementById("hotels").innerHTML = html;
            }
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
