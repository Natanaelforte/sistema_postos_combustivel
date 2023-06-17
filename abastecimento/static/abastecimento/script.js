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

$(document).ready(function() {
    carregarSelectBombas();
    carregarSelectCombustivel();
    carregarSelectColaborador()
})