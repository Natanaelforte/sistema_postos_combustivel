from base.forms import BasePadraoForm
from .choices.choices_combustivel import C_TIPO_DE_COMBUSTIVEL
from .models import Combustivel
from django import forms


class CombustivelForm(BasePadraoForm):
    tipo_de_combustivel = forms.ChoiceField(
        choices=(C_TIPO_DE_COMBUSTIVEL),
        label=('Combustivel'),
        widget=forms.Select(attrs={'class': 'combustivel-tipo'}),
    )
    class Meta:
        model = Combustivel
        fields = ['tipo_de_combustivel']
