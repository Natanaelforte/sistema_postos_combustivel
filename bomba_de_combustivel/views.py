from django.urls import reverse, reverse_lazy
from django.views.generic import  DeleteView

from base.views import CreateBaseView, ListBaseView, UpdateBaseView
from .forms import BombaForm
from .models import Bomba


class BombaListView(ListBaseView):
    model = Bomba
    template_name = 'bomba_de_combustivel/list.html'


class BombaCreateView(CreateBaseView):
    model = Bomba
    template_name = 'bomba_de_combustivel/forms.html'
    form_class = BombaForm

    def get_success_url(self):
        return reverse('bomba_de_combustivel:list')


class BombaUpdateView(UpdateBaseView):
    model = Bomba
    fields = ['numero', 'tanques']
    template_name = 'bomba_de_combustivel/update.html'

    def get_success_url(self):
        return reverse('bomba_de_combustivel:list')


class BombaDeleteView(DeleteView):
    model = Bomba
    template_name = 'bomba_de_combustivel/delete.html'
    success_url = reverse_lazy("bomba_de_combustivel:list")
