from django.forms import ModelForm

from tanque.models import Tanque
from .models import Bomba


class BombaForm(ModelForm):
    class Meta:
        model = Bomba
        fields = ['numero', 'tanques']

    def __init__(self, *args, **kwargs):
        posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)

        if posto_pk:
            tanques = Tanque.objects.filter(posto__pk=posto_pk)

            self.fields['tanques'].queryset = tanques
