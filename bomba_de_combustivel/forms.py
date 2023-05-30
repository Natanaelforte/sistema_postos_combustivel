from django.forms import ModelForm
from .models import Bomba


class BombaForm(ModelForm):
    class Meta:
        model = Bomba
        fields = ['posto', 'numero', 'tanques']
