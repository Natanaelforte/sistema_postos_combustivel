from base.forms import BasePadraoForm
from colaborador.models import Colaborador
from funcao.models import Funcao
from django import forms


class ColaboradorForm(BasePadraoForm):
    nome = forms.CharField(
        label=('Nome'),
        widget=forms.CharField(attrs={'class': 'colaborador-nome', 'placeholder': 'Nome...'})
    )
    cpf = forms.CharField(
        label=('CPF'),
        widget=forms.CharField(attrs={'class': 'colaborador-cpf', 'placeholder': 'CPF...'})
    )
    contato = forms.CharField(
        label=('Contato'),
        widget=forms.CharField(attrs={'class': 'colaborador-Contato', 'placeholder': 'Contato...'})
    )
    endereco = forms.CharField(
        label=('Endereço'),
        widget=forms.CharField(attrs={'class': 'colaborador-endereco', 'placeholder': 'Endereço...'})
    )
    funcao = forms.ModelChoiceField(
        label=('Função'),
        widget=forms.ChoiceField(attrs={'class': 'colaborador-funcao', 'placeholder': 'Função...'})
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
