from django.contrib.auth.forms import AuthenticationForm
from django import forms

from posto.models import Posto


class AcessoForm(AuthenticationForm):
    posto = forms.ModelChoiceField(queryset=Posto.objects.none(), widget=forms.Select(), required=False)

    def __init__(self, request=None, *args, **kwargs):
        super(AcessoForm, self).__init__(request, *args, **kwargs)

        if self.data and 'posto' in self.data:
            self.fields['posto'].queryset = Posto.objects.filter(id=self.data['posto'])
