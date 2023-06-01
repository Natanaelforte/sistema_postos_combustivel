from base.forms import BasePadraoForm
from .models import Funcao


class FuncaoForm(BasePadraoForm):
    class Meta:
        model = Funcao
        fields = ['codigo', 'descricao']
