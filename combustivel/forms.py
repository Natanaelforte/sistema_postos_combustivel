from base.forms import BasePadraoForm
from .models import Combustivel


class CombustivelForm(BasePadraoForm):
    class Meta:
        model = Combustivel
        fields = ['tipo_de_combustivel']
