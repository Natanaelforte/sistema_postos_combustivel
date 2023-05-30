from django.views.generic import ListView
from funcao.models import Funcao


class FuncaoListViewl(ListView):
    model = Funcao
    template_name = 'funcao/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset
