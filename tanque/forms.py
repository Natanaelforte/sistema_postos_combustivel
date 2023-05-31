from django.forms import ModelForm

from combustivel.models import Combustivel
from .models import Tanque


class TanqueForm(ModelForm):
    class Meta:
        model = Tanque
        fields = ['combustivel', 'quantidade_litros']

    def __init__(self, *args, **kwargs):
        posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)

        if posto_pk:
            combustivel = Combustivel.objects.filter(posto__pk=posto_pk)

            self.fields['tanques'].queryset = combustivel
