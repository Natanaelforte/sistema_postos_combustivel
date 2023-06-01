from base.forms import BasePadraoForm
from bomba_de_combustivel.models import Bomba
from colaborador.models import Colaborador
from combustivel.models import Combustivel
from .models import Abastecimento


class AbastecimentoForm(BasePadraoForm):
    class Meta:
        model = Abastecimento
        fields = ['colaborador', 'bomba', 'combustivel', 'litros_abastecido', 'data']

    def __init__(self, *args, **kwargs):
        posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)

        if posto_pk:
            colaborador = Colaborador.objects.filter(posto__pk=posto_pk)
            combustivel = Combustivel.objects.filter(posto__pk=posto_pk)
            bomba = Bomba.objects.filter(posto__pk=posto_pk)

            self.fields['colaborador'].queryset = colaborador
            self.fields['combustivel'].queryset = combustivel
            self.fields['bomba'].queryset = bomba
