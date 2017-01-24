/**
 * Created by pc on 24.01.17.
 */

$("#loginForm").submit(function (event) {
    event.preventDefault();
    var csrftoken = $.cookie('csrftoken');
    var data = {
        username: $('#username').val(),
        password: $('#password').val(),
    };
    $.ajax({
        type: "POST",
        url: "/api/login/",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }).then(function (resp) {
                    console.log('done')
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
                location.reload();
            });
})
