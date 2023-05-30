from django.views.generic import ListView
from abastecimento.models import Abastecimento


class AbastecimentoListViewl(ListView):
    model = Abastecimento
    template_name = 'abastecimento/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset