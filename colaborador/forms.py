from base.forms import BasePadraoForm
from colaborador.models import Colaborador
from funcao.models import Funcao


class ColaboradorForm(BasePadraoForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'contato', 'endereco', 'funcao']

    def __init__(self, *args, **kwargs):
        posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)

        if posto_pk:
            funcao = Funcao.objects.filter(posto__pk=posto_pk)

            self.fields['funcao'].queryset = funcao
