function carregarSelectPost() {
    $.ajax({
        url: urlApiPostos,
        type: "GET",
        data: {
            username: $('#id_username').val()
        },
        dataType: "json",
        success: function (dados) {
            // console.log(dados[idx])

            $(dados).each(function (idx, item) {
                // console.log(dados[idx])
                var option = new Option(`${dados[idx].fields['cnpj']} - ${dados[idx].fields['razao_social']}` , dados[idx].pk)

                $('#id_posto').append(option)
            })
        }, error: function (dados) {
            console.log('deu erro no api postos.')
        }
    })
}

$('#id_username').on('focusout', carregarSelectPost)
