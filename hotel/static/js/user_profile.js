/**
 * Created by pc on 19.01.17.
 */
$(document).ready(function () {
    getReservations()


});

function deleteReservation() {
    $(".destroy").click(function () {
        var csrftoken = $.cookie('csrftoken');
        var reservation = this.value;
        $.ajax({
            type: "DELETE",
            url: "/api/reservations/" + reservation + "/delete/",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        })
        getReservations()

    });
}

function getReservations() {
    $.ajax({
        type: "GET",
        url: "/api/profile/",
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    })
        .done(function (data) {
            reservations = data.reservations;
            profile = data.profile;
            html = "";
            for (var i = 0, len = reservations.length; i < len; i++) {
                html +=
                    "Start Date: " + reservations[i].start_date + "</br></<br>" +
                    "End of Reservation " + reservations[i].end_date + "</br></br>" +
                    "Room: " + reservations[i].room_name + "</br></br>" +
                    "<button type=\"button\" class=\"btn btn-danger destroy \"" +
                    " value='" + reservations[i].pk + "'> Abandon reservation </button></br>"
                document.getElementById("reservations").innerHTML = html;
            }
            html = "<img src=\" " + profile.photo + "\" alt=\"...\">"
            document.getElementById("thumbnail").innerHTML = html;
            html = ""
            html +=
                "<li class=\"list-group-item\">Name: " + profile.name + "</li><br>" +
                "<li class=\"list-group-item\">Address: " + profile.addres + " </li><br>" +
                "<li class=\"list-group-item\">Telephone: " + profile.telephone + " </li><br>"

            document.getElementById("profileList").innerHTML = html;
            deleteReservation()

        })
        .fail(function (data) {
            console.log("error", data);
        });
}