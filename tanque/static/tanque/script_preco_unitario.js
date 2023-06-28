function pegarValorUnitario() {
    $.ajax({
        headers: {'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ASPSESSIONIDASDCBTRA=GINMMEEBHFIENPHHIHOEBBKD'},
        url: urlPrecoBuscar,
        type: 'POST',
        data: {
            URL: 'http://comprasnet.gov.br/livre/Resultado/conrelit01.asp',
            payloads: 'co_uasg=943001'
        },
        success: function (data) {
            $('#preco-unitario').val(data.preco.texto)
        }, error: function (data) {
            alert('deu erro!')
        }

    })
}