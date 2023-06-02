

function carregarSelectPost() {
    $.ajax({
        url: urlApiPostos,
        type: "GET",
        data: {
            username: $('#id_username').val()
        },
        dataType: "json",
        success: function (dados) {
            $('#id_posto').find('option').remove()

            $(dados).each(function (idx, item) {
                var option = new Option(`${dados[idx].fields['cnpj']} - ${dados[idx].fields['razao_social']}` , dados[idx].pk)

                $('#id_posto').append(option)
            })

            if (dados.length > 0) {
                $('#id_posto').css({display: 'block'});
            } else {
                $('#id_posto').css({display: 'None'});
                // mensagem
            }

        }, error: function (dados) {
            console.log('deu erro no api postos.')
        }
    })
}


function onInputUsername() {
    if ($('#id_username').val().length >= 5)  {
        carregarSelectPost()
    }
}

$(document).ready(function() {
    $("#id_username").on("input", onInputUsername)
})
