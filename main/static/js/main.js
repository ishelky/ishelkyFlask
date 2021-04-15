function check_val(inp, error_div, text_error) {
    inp.removeClass("is-invalid");
    console.log(inp)
    console.log(error_div)
    if ($.trim(inp.val()).length > 0) {
        return inp.val();
    } else {
        inp.addClass("is-invalid")
        error_div.addClass("alert alert-danger");
        error_div.append("<div >" + text_error + "</div>");
        return false;
    }

}

function randomInteger(min, max) {
    var rand = min + Math.random() * (max - min)
    rand = Math.round(rand);
    return rand;
}

var k1 = randomInteger(8, 43)

function check_statick_form(form) {
    var nameObj = form.find(".name");
    var textObj = form.find(".text");
    var emailObj = form.find(".email");
    var errorObj = form.find(".error");
    var row = form.find(".row");
    errorObj.empty()
    errorObj.removeClass("alert alert-danger");
    var fetaObj = false
    if (row.children().length == 3) {
        row.append("<label class=\"form-group has-float-label col-12\">" +
            "<input class=\"form-control feta\" type=\"text\" />" +
            "<span>Подтвердите что Вы не робот, введите число: " + k1 + "</span>" +
            "</label>")
    } else {
        var fetaObj = form.find(".feta");
        var num = check_val(fetaObj, errorObj, "Поле проверки не заполненно")
    }
    var name = check_val(nameObj, errorObj, "Вы не ввели Имя");
    var text = check_val(textObj, errorObj, "Вы не ввели сообщение");
    var email = check_val(emailObj, errorObj, "Вы не ввели email")
    console.log(name, text, email, num)
    if (name && text && email && num) {
        var dt = {
            "grata": k1,
            "contact": email,
            "name": name,
            "num": num,
            "text": text
        };
        $.ajax({
            url: '/api/mail',
            data: dt,
            type: 'POST',
            success: function (res) {
                if (res.result) {
                    errorObj.append("<div class=\"alert alert-success\" role=\"alert\">Сообщение отправлено, мы свяжемся с вами в ближайшее время.</div>")
                } else {
                    errorObj.append("<div class=\"alert alert-danger\" role=\"alert\">" + res.text + "</div>")
                }
                ;

            },
            error: function (error) {
                errorObj.append("<div class=\"alert alert-danger\" role=\"alert\">Что то пошло не так ((</div>")
            }
        })
    } else {
        return
    }


}



$(document).ready(function () {


    $("#send_popup_mail").click(function () {
        var grata = $("#grata");
        $("#error_popup_mail").empty()
        var InputContact = check_val($("#InputContact_popup_mail"), $("#error_popup_mail"), "Поле контакт не заполненно");
        var InputName = check_val($("#InputName_popup_mail"), $("#error_popup_mail"), "Поле Имя не заполненно");
        var num = grata.data("num");
        var InputNun = false
        if (grata.children().length == 0) {
            grata.append("<label for='InputNun_popup_mail '>Подтвердите что Вы не робот, введите число: " + num + "</label>" +
                "<input type='text' class='form-control is-invalid' id='InputNun_popup_mail' >")
        } else {
            var InputNun = check_val($("#InputNun_popup_mail"), $("#error_popup_mail"), "Поле проверки не заполненно");
        }

        if (InputContact && InputName && InputNun) {
            var dt = {
                "grata": num,
                "contact": InputContact,
                "name": InputName,
                "num": InputNun,
                "text": $("#InputMessage_popup_mail").val()
            };
            $.ajax({
                url: '/api/mail',
                data: dt,
                type: 'POST',
                success: function (res) {
                    if (res.result) {
                        $("#error_popup_mail").append("<div class=\"alert alert-success\" role=\"alert\">Сообщение отправлено, мы свяжемся с вами в ближайшее время.</div>")
                    } else {
                        $("#error_popup_mail").append("<div class=\"alert alert-danger\" role=\"alert\">" + res.text + "</div>")
                    }
                    ;

                },
                error: function (error) {
                    $("#error_popup_mail").append("<div class=\"alert alert-danger\" role=\"alert\">Что то пошло не так ((</div>")
                }
            })
        } else {
            return
        }


    });


    $(".form_statick_front").on('click', function (event) {
        event.stopPropagation();
        event.stopImmediatePropagation();
        check_statick_form($(this).parent())
        event.preventDefault();
    });


});

