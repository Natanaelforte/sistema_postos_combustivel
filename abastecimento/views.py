from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from abastecimento.forms import AbastecimentoForm
from abastecimento.models import Abastecimento
from base.views import CreateBaseView, ListBaseView, UpdateBaseView


class AbastecimentoListView(ListBaseView):
    model = Abastecimento
    template_name = 'abastecimento/list.html'


class AbastecimentoCreateView(CreateBaseView):
    model = Abastecimento
    template_name = 'abastecimento/forms.html'
    form_class = AbastecimentoForm


    def get_success_url(self):
        return reverse('abastecimento:list')


class AbastecimentoUpdateView(UpdateBaseView):
    model = Abastecimento
    fields = ['colaborador', 'bomba', 'combustivel', 'litros_abastecido', 'data']
    template_name = 'abastecimento/update.html'

    def get_success_url(self):
        return reverse('abastecimento:list')


class AbastecimentoDeleteView(DeleteView):
    model = Abastecimento
    template_name = 'abastecimento/delete.html'
    success_url = reverse_lazy("abastecimento:list")
