from django.forms import ModelForm
from .models import Tanque


class TanqueForm(ModelForm):
    class Meta:
        model = Tanque
        fields = ['posto', 'combustivel', 'quantidade_litros']
