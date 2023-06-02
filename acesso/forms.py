from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

from posto.models import Posto


class AcessoForm(AuthenticationForm):
    posto = forms.ModelChoiceField(queryset=Posto.objects.none(), widget=forms.Select(
        attrs={'class': 'ap-input-select'}),
        required=False, )

    username = UsernameField(widget=forms.TextInput
    (attrs={"autofocus": True, 'class': 'ap-input', 'placeholder': 'Usuário'}))

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
        attrs={"autocomplete": "current-password", 'class': 'ap-input', 'placeholder': 'Senha'}),
    )

    def __init__(self, request=None, *args, **kwargs):
        super(AcessoForm, self).__init__(request, *args, **kwargs)

        if self.data and 'posto' in self.data:
            self.fields['posto'].queryset = Posto.objects.filter(id=self.data['posto'])
