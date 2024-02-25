$(document).ready(function (){
    $('#FormAuth').submit(function (e) {
        e.preventDefault();
        let form = $(this)
        let csrfmiddlewaretoken = form.find('input[name = "csrfmiddlewaretoken"]').val()
        let login = form.find('input[name = "login"]').val()
        let password = form.find('input[name = "password"]').val()

        $.ajax({
            type: "POST",
            url: "/auth",
            data: {
                "csrfmiddlewaretoken": csrfmiddlewaretoken,
                "login": login,
                "password": password,
            },
            success: function (response) {
                console.log(response)
            }
        })
    })
    $('#FormReg').submit(function (e) {
        e.preventDefault();
        let form =$(this);
        let csrfmiddlewaretoken = form.find('input[name = "csrfmiddlewaretoken"]').val()
        let login = form.find('input[name = "login"]').val()
        let name = form.find('input[name = "name"]').val()
        let surname = form.find('input[name = "surname"]').val()
        let email = form.find('input[name = "email"]').val()
        let password = form.find('input[name = "password"]').val()
        let password2 = form.find('input[name = "password2"]').val()

        if (password == password2){
            $.ajax({
                type: "POST",
                url: "/auth/reg",
                data: {
                    "csrfmiddlewaretoken": csrfmiddlewaretoken,
                    "name": name,
                    "surname": surname,
                    "email": email,
                    "login": login,
                    "password": password,
                    
                },
                success: function (response) {
                    if (response.status == 'ok'){
                        $('#result').text("Регистрация прошла успешно!")
                    } else if (response.status == 'NoLogin'){
                        $('#result').text("Регистрация не прошла! Неверный логин")
                    } else {
                        $('#result').text("Что-то пошло не так!")
                    }
                }
            })
        } else {
            $('#result').text("Пароль не совпадает")
        }
            

    })
})
    