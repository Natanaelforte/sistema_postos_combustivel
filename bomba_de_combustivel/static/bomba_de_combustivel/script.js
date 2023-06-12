function carregarTabela() {
    $.ajax({
        url: urlTableBusca,
        type: 'GET',
        data: {
            search: $('#search').val()
        },
        success: function (data) {
            $('#tabela').html(data.tabela)
        }
    })
}