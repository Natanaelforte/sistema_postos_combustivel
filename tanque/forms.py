from base.forms import BasePadraoForm
from combustivel.models import Combustivel
from .models import Tanque


class TanqueForm(BasePadraoForm):
    class Meta:
        model = Tanque
        fields = ['combustivel', 'quantidade_litros']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.posto_pk:
            combustivel = Combustivel.objects.filter(posto__pk=self.posto_pk)

            self.fields['combustivel'].queryset = combustivel
