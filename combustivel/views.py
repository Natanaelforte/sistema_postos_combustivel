from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from base.views import CreateBaseView, ListBaseView, UpdateBaseView
from combustivel.forms import CombustivelForm
from combustivel.models import Combustivel


class CombustivelListView(ListBaseView):
    model = Combustivel
    template_name = 'combustivel/list.html'


class CombustivelCreateView(CreateBaseView):
    model = Combustivel
    template_name = 'combustivel/forms.html'
    form_class = CombustivelForm

    def get_success_url(self):
        return reverse('combustivel:list')


class CombustivelUpdateView(UpdateBaseView):
    model = Combustivel
    template_name = 'combustivel/update.html'
    form_class = CombustivelForm

    def get_success_url(self):
        return reverse('combustivel:list')


class CombustivelDeleteView(DeleteView):
    model = Combustivel
    template_name = 'combustivel/delete.html'
    success_url = reverse_lazy("combustivel:list")
