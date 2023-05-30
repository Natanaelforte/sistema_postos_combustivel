from django.forms import ModelForm
from .models import Combustivel


class CombustivelForm(ModelForm):
    class Meta:
        model = Combustivel
        fields = ['posto', 'tipo_de_combustivel']
