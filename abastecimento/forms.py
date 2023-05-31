from django.forms import ModelForm
from .models import Abastecimento


class AbastecimentoForm(ModelForm):
    class Meta:
        model = Abastecimento
        fields = ['colaborador', 'bomba', 'combustivel', 'litros_abastecido', 'data']
