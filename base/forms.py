from django.forms import ModelForm


class BasePadraoForm(ModelForm):
    posto_pk = None

    def __init__(self, *args, **kwargs):
        self.posto_pk = kwargs.pop('posto_pk', None)

        super().__init__(*args, **kwargs)
