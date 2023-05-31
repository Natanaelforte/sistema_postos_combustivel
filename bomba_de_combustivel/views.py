from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView

from base.views import CreateBaseView, ListBaseView
from .forms import BombaForm
from .models import Bomba


class BombaListView(ListBaseView):
    model = Bomba
    template_name = 'bomba_de_combustivel/list.html'


class BombaCreateView(CreateBaseView):
    model = Bomba
    template_name = 'bomba_de_combustivel/forms.html'
    form_class = BombaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'posto_pk': self.request.session['posto']})

        return kwargs

    def get_success_url(self):
        return reverse('bomba_de_combustivel:list')


class BombaUpdateView(UpdateView):
    model = Bomba
    fields = ['numero', 'tanques']
    template_name = 'bomba_de_combustivel/update.html'

    def get_success_url(self):
        return reverse('bomba_de_combustivel:list')


class BombaDeleteView(DeleteView):
    model = Bomba
    template_name = 'bomba_de_combustivel/delete.html'
    success_url = reverse_lazy("bomba_de_combustivel:list")
