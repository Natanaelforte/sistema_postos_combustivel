from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView

from base.views import CreateBaseView, ListBaseView
from tanque.forms import TanqueForm
from tanque.models import Tanque


class TanqueListView(ListBaseView):
    model = Tanque
    template_name = 'tanque/list.html'


class TanqueCreateView(CreateBaseView):
    model = Tanque
    template_name = 'tanque/forms.html'
    form_class = TanqueForm

    def get_success_url(self):
        return reverse('tanque:list')


class TanqueUpdateView(UpdateView):
    model = Tanque
    fields = ['combustivel', 'quantidade_litros']
    template_name = 'tanque/update.html'

    def get_success_url(self):
        return reverse('tanque:list')


class TanqueDeleteView(DeleteView):
    model = Tanque
    template_name = 'tanque/delete.html'
    success_url = reverse_lazy("tanque:list")
