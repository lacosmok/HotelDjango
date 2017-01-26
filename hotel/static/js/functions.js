/**
 * Created by pc on 16.12.16.

});
 */

 $(function () {
     $(".date").datepicker({
         dateFormat: "yy-mm-dd"
     });
 })

$(document).ready(function () {
    var buttonStatus = $.cookie("buttonStatus")
    if (buttonStatus == undefined) {
        $.cookie("buttonStatus", "false");
    }
    var elem = document.getElementById("checkCookie");
    elem.innerHTML = ($.cookie("buttonStatus"))

});
$("#checkCookie").on('click', function () {
    var buttonStatus = $.cookie("buttonStatus")
    switch (buttonStatus) {
        case("true"):
            $.cookie("buttonStatus", false);
            console.log("click true");
            break;
        case ("false"):
            $.cookie("buttonStatus", true);
            console.log("click false");
            break;
    }
    var elem = document.getElementById("checkCookie");
    elem.innerHTML = ($.cookie("buttonStatus"));

});



