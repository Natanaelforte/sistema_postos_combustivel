from django.views.generic import ListView
from combustivel.models import Combustivel


class CombustivelListViewl(ListView):
    model = Combustivel
    template_name = 'combustivel/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset
