from django.views.generic import ListView
from .models import Bomba


class BombaListViewl(ListView):
    model = Bomba
    template_name = 'bomba_de_combustivel/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset
