from base.forms import BasePadraoForm
from django import forms

from .models import Funcao


class FuncaoForm(BasePadraoForm):
    codigo = forms.CharField(
        label=('Código'),
        widget=forms.TextInput(attrs={'class': 'funcao-cidigo'})
    )
    descricao = forms.CharField(
        label=('Descrição'),
        widget=forms.TextInput(attrs={'class': 'funcao-descricao'})
    )

    class Meta:
        model = Funcao
        fields = ['codigo', 'descricao']
