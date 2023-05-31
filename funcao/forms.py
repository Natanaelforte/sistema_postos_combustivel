from django.forms import ModelForm
from .models import Funcao


class FuncaoForm(ModelForm):
    class Meta:
        model = Funcao
        fields = ['codigo', 'descricao']
