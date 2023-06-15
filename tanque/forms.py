from base.forms import BasePadraoForm
from django import forms

from combustivel.models import Combustivel
from .models import Tanque


class TanqueForm(BasePadraoForm):
    combustivel = forms.ModelChoiceField(
        label=('Combustível'),
        widget=forms.Select(attrs={'class': 'tanque-combustivel', 'placeholder': 'Combustível...'}),
        queryset=Tanque.objects.none()
    )
    quantidade_litros = forms.IntegerField(
        label=("Litros"),
        widget=forms.NumberInput(
            attrs={'class': 'tanque-quantidade_litros', 'placeholder': 'Quantidade de Litros...'}
        ),
    )


    class Meta:
        model = Tanque
        fields = ['combustivel', 'quantidade_litros']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.posto_pk:
            combustivel = Combustivel.objects.filter(posto__pk=self.posto_pk)

            self.fields['combustivel'].queryset = combustivel
