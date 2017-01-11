/**
 * Created by pc on 16.12.16.
 */

$(function () {
    console.log("działą")
    $(".date").datepicker({
        dateFormat: "yy-mm-dd"
    });
});



$( "#reservationForm" ).submit(function( event ) {
    event.preventDefault();
    alert("wow")
    var csrftoken = $.cookie('csrftoken');
    var data = {start_date: $('#start_date').val(),
            end_date: $('#end_date').val(),
            room: $('#room').val()
        };
        console.log(data);
    $.ajax({
        type: "POST",
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
        .done(function(resp) {
    console.log(resp)
            alert("wow")
  })
  .fail(function() {
    console.log(resp)
      alert("wow")
  })
  .always(function() {
    console.log(resp)
      alert("wow")
  });

    console.log("its working")

});