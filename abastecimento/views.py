from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from abastecimento.forms import AbastecimentoForm
from abastecimento.models import Abastecimento
from base.views import CreateBaseView, ListBaseView, UpdateBaseView, ActionBaseView, TableBaseView
from bomba_de_combustivel.models import Bomba
from colaborador.models import Colaborador
from combustivel.models import Combustivel


class AbastecimentoListView(ListBaseView):
    model = Abastecimento
    template_name = 'abastecimento/list.html'


class AbastecimentoAbastecerView(ActionBaseView):
    model = Abastecimento

    def _try_get_param(self, param_name):
        try:
           return self.request.POST.get(param_name)
        except:
            raise Exception(f'{param_name.title()} não informada.')

    def _try_get_instance(self, class_name, pk):
        try:
            return class_name.objects.get(pk=pk)
        except:
            raise Exception(f'{class_name} ou {pk}, não informados.')

    def do_action(self):
        bomba_id = self._try_get_param('bomba')
        combustive_id = self._try_get_param('combustivel')
        colaborador_id = self._try_get_param('colaborador')

        bomba = self._try_get_instance(Bomba, bomba_id)
        combustivel = self._try_get_instance(Combustivel, combustive_id)
        colaborador = self._try_get_instance(Colaborador, colaborador_id)

        litros_abastecido = self._try_get_param('litros_abastecido')

        try:
            Abastecimento.objects.create(
                bomba=bomba, combustivel=combustivel, colaborador=colaborador, litros_abastecido=litros_abastecido
            )
        except:
            raise Exception('Não foi possivel criar o abastecimento.')


class AbastecimentoUpdateView(UpdateBaseView):
    model = Abastecimento
    form_class = AbastecimentoForm
    template_name = 'abastecimento/update.html'

    def get_success_url(self):
        return reverse('abastecimento:list')


class AbastecimentoDeleteView(DeleteView):
    model = Abastecimento
    template_name = 'abastecimento/delete.html'
    success_url = reverse_lazy("abastecimento:list")


class AbastecimentoTableView(TableBaseView):
    model = Abastecimento
    template_name = 'colaborador/table.html'

    def _try_get_param(self, param_name):
        try:
           return self.request.POST.get(param_name)
        except:
            pass

    def _try_get_instance(self, class_name, pk):
        try:
            return class_name.objects.get(pk=pk)
        except:
            pass


    def get_queryset(self):

        queryset = super().get_queryset()

        bomba_id = self._try_get_param('bomba')

        if bomba_id:
            queryset = queryset.filter(bomba__id=bomba_id)

        combustive_id = self._try_get_param('combustivel')

        if combustive_id:
            queryset = queryset.filter(combustive_id=combustive_id)

        colaborador_id = self._try_get_param('colaborador')

        if colaborador_id:
            queryset = queryset.filter(colaborador_id=colaborador_id)


        return queryset