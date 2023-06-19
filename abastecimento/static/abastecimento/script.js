function carregarSelectBombas() {
    $.ajax({
        url: urlApiBombas,
        type: "GET",
        data: {

        },
        dataType: "json",
        success: function (dados) {
            var select = document.getElementById('card-campo-bomba');


            for (var i in dados) {
                $(select).append("<option value=" + dados[i].pk + ">Bomba  " + dados[i].fields.numero + "</option>");
            }

            $(select).val(dados[1]);

        }, error: function (dados) {
            console.log('deu erro no api postos.')
        }
    })
}

function carregarSelectCombustivel() {
    $.ajax({
        url: urlApiCombustiveis,
        type: "GET",
        data: {

        },
        dataType: "json",
        success: function (dados) {
            var select = document.getElementById('card-campo-combustivel');

            var combustivel = dados.resultados

            for (var i in combustivel) {
                $(select).append("<option value=" + combustivel[i].pk + ">" + combustivel[i].label + "</option>");
            }

            $(select).val(dados[1]);

        }, error: function (dados) {
            console.log('deu erro no api postos.')
        }
    })
}

function carregarSelectColaborador() {
    $.ajax({
        url: urlApiColaboradores,
        type: "GET",
        data: {

        },
        dataType: "json",
        success: function (dados) {
            var select = document.getElementById('card-campo-colaborador');


            for (var i in dados) {
                $(select).append("<option value=" + dados[i].pk + ">" + dados[i].fields.nome + "</option>");
            }

            $(select).val(dados[1]);

        }, error: function (dados) {
            console.log('deu erro no api postos.')
        }
    })
}

function CriarAbastecimento() {
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: `${urlApiAbastecimento}?data=now`,
        type: "POST",
        data: {
            bomba: $('#card-campo-bomba').val(),
            combustivel: $('#card-campo-combustivel').val(),
            colaborador: $('#card-campo-colaborador').val(),
            litros_abastecido: $('#card-campo-litros').val(),
        },
        dataType: "json",
        success: function (dados) {
            if (dados.resposta == 'sim') {
                $('#card-campo-litros').val(0);
            } else {
                alert(dados.menssagem)
            }

        }
    })
}

function carregarTabela() {
    $.ajax({
        url: urlTableBusca,
        type: 'GET',
        data: {
            bomba: $('#card-campo-bomba').val(),
            combustivel: $('#card-campo-combustivel').val(),
            colaborador: $('#card-campo-colaborador').val(),
        },
        success: function (data) {
            $('#tabela').html(data.tabela)
        }
    })
}

$(document).ready(function() {
    carregarSelectBombas();
    carregarSelectCombustivel();
    carregarSelectColaborador()
})