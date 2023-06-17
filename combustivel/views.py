import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from base.views import CreateBaseView, ListBaseView, UpdateBaseView, DeleteBaseView, TableBaseView
from combustivel.choices.choices_combustivel import C_TIPO_DE_COMBUSTIVEL
from combustivel.forms import CombustivelForm
from combustivel.models import Combustivel


class CombustivelListView(ListBaseView):
    model = Combustivel
    template_name = 'combustivel/list.html'


class CombustivelTableView(TableBaseView):
    model = Combustivel
    search_fields = [('tipo_de_combustivel', C_TIPO_DE_COMBUSTIVEL), ]
    template_name = 'combustivel/table.html'


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


class CombustivelDeleteView(DeleteBaseView):
    model = Combustivel
    template_name = 'combustivel/delete.html'
    success_url = reverse_lazy("combustivel:list")


class CombustivelSelectView(ListBaseView):
    model = Combustivel
    template_name = 'abastecimento/list.html'

    def get(self, request, *args, **kwargs):
        combustiveis = self.get_queryset()

        dict_combustiveis = []

        for comb in combustiveis:
            dict_combustiveis.append({
                'pk': comb.pk,
                'label': comb.combustivel_tipo
            })

        return JsonResponse({'resultados': dict_combustiveis})
