$(document).ready(function (){
    function submit_email(e){
        e.preventDefault();
        let form = $(this);
        let len = form.find('input[name="len"]').val();
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            type: 'POST',
            url: '/api',
            data: {
                csrfmiddlewaretoken: csrftoken,
                count_email: len,
                action: 'generate-email'
            },
            success: function (response) {
                for (let i = 0; i < response.data_email.length; i++){
                    let section = document.querySelector("#emails")
                    let p = document.createElement("p")
                    p.textContent = response.data_email[i]
                    section.appendChild(p)
                }
                
            },
            error: function (response) {

            }
        })
    }
    $('#form_generate_email').submit(submit_email)

    $('.send-btn').click(function (){
        $.ajax({
            type: 'POST',
            url: '/api',
            data: {
                action: 'generate-password',
                len_password: $('#len_password').val(), 
                count_password: $('#count_password').val(), 
                csrfmiddlewaretoken: $('meta[name="csrf-token"]').attr('content')
            },
            success: function(response){
                for (let i = 0; i < response.data_password.length; i++){
                    let section = document.querySelector('#passwords')
                    let p = document.createElement('p')
                    p.textContent = response.data_password[i]
                    section.appendChild(p)}
            },
            error: function(response){}
        })
    })
})