from django.urls import reverse
from django.views.generic import ListView, CreateView

from tanque.forms import TanqueForm
from tanque.models import Tanque


class TanqueListViewl(ListView):
    model = Tanque
    template_name = 'tanque/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset


class TanqueCreate(CreateView):
    model = Tanque
    template_name = 'tanque/forms.html'
    form_class = TanqueForm

    def get_success_url(self):
        return reverse('bomba_de_combustivel:bomba')
