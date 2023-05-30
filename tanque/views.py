from django.views.generic import ListView
from tanque.models import Tanque


class TanqueListViewl(ListView):
    model = Tanque
    template_name = 'tanque/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset