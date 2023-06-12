from django import forms

from base.forms import BasePadraoForm
from tanque.models import Tanque
from .models import Bomba


class BombaForm(BasePadraoForm):
    numero = forms.IntegerField(
        label=("Número"),
        widget=forms.NumberInput(
            attrs={'class': 'ap-input-numero', 'placeholder': 'Número...'}
        ),
    )
    tanques = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'ap-input-tanques'}),
              queryset=Tanque.objects.none())

    class Meta:
        model = Bomba
        fields = ['numero', 'tanques']

    def __init__(self, *args, **kwargs):
        posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)

        if posto_pk:
            tanques = Tanque.objects.filter(posto__pk=posto_pk)

            self.fields['tanques'].queryset = tanques
