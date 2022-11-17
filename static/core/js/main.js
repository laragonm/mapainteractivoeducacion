let csrf_token = null;

function showLoad(option = true) {
    if (option) {
        $("#loader-wrapper").css("display", "block");
        $(".section-left").show("slide", {direction: "left"}, 250);
        $(".section-right").show("slide", {direction: "right"}, 250, function () {
            $("#loader").fadeIn();
        });
    } else {
        $("#loader").hide();
        $("#loader").css("display", "none");
        $(".section-left").hide("slide", {direction: "left"}, 750);
        $(".section-right").hide("slide", {direction: "right"}, 750, function () {
            $("#loader-wrapper").css("display", "none");
        });
    }
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    }
});

function reload(time) {
    time = time || 1000;
    setTimeout(function () {
        location.reload()
    }, time)
}