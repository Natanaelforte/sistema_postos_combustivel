from django.forms import ModelForm

from colaborador.models import Colaborador


class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['posto', 'nome', 'cpf', 'contato', 'endereco', 'funcao']
