from base.forms import BasePadraoForm
from colaborador.models import Colaborador
from funcao.models import Funcao
from django import forms


class ColaboradorForm(BasePadraoForm):
    nome = forms.CharField(
        label=('Nome'),
        widget=forms.TextInput(attrs={'class': 'colaborador-nome'})
    )
    cpf = forms.CharField(
        label=('CPF'),
        widget=forms.TextInput(attrs={'class': 'colaborador-cpf'})
    )
    contato = forms.CharField(
        label=('Contato'),
        widget=forms.TextInput(attrs={'class': 'colaborador-Contato'})
    )
    endereco = forms.CharField(
        label=('Endereço'),
        widget=forms.TextInput(attrs={'class': 'colaborador-endereco'})
    )
    funcao = forms.ModelChoiceField(
        label=('Função'),
        widget=forms.Select(attrs={'class': 'colaborador-funcao'}),
        queryset=Colaborador.objects.none()
    )

    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'contato', 'endereco', 'funcao']

    def __init__(self, *args, **kwargs):
        posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)

        if posto_pk:
            funcao = Funcao.objects.filter(posto__pk=posto_pk)

            self.fields['funcao'].queryset = funcao
