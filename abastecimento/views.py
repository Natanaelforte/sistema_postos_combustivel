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
        combustivel_id = self._try_get_param('combustivel')
        colaborador_id = self._try_get_param('colaborador')

        bomba = self._try_get_instance(Bomba, bomba_id)
        combustivel = self._try_get_instance(Combustivel, combustivel_id)
        colaborador = self._try_get_instance(Colaborador, colaborador_id)

        litros_abastecido = self._try_get_param('litros_abastecido')

        posto = self._get_instance_posto()

        try:
            Abastecimento.objects.create(
                bomba=bomba, combustivel=combustivel, colaborador=colaborador, litros_abastecido=litros_abastecido,
                posto=posto
            )
        except Exception as e:
            print(str(e))

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
    template_name = 'abastecimento/table.html'

    def _try_get_param(self, param_name):
        try:
           return self.request.GET.get(param_name)
        except:
            pass

    def get_queryset(self):

        queryset = super().get_queryset()

        bomba_id = self._try_get_param('bomba')

        if bomba_id:
            queryset = queryset.filter(bomba__id=bomba_id)

        combustivel_id = self._try_get_param('combustivel')

        if combustivel_id:
            queryset = queryset.filter(combustivel_id=combustivel_id)

        colaborador_id = self._try_get_param('colaborador')

        if colaborador_id:
            queryset = queryset.filter(colaborador_id=colaborador_id)

        return queryset


class AbastecimentoValorTotal(ActionBaseView):
    model = Abastecimento
    template_name = 'abastecimento/list.html'

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

    def calcular_valor(self, valor_vigente, litros):
        valor = valor_vigente * litros

        return valor

    def post(self, request, *args, **kwargs):
        data = {}
        combustivel_id = self._try_get_param('combustivel')
        combustivel = self._try_get_instance(Combustivel, combustivel_id)

        valor_vigente = combustivel.valor_vigente
        valor_vigente = float(valor_vigente)

        litros = self.request.POST.get('litros', 0)
        litros = float(litros)

        try:
            valor = self.calcular_valor(valor_vigente=valor_vigente, litros=litros)
            data['resposta'] = 'sim'
            data['valor'] = f'Total: R$ {valor:.2f}'
        except Exception as e:
            data['resposta'] = 'não'
            data['mensagem'] = 'Não foi possivel calcular o valor'

            """mostrar mensagem de erro 'Erro ao tentar salvar {str(e)}' e a resposta não"""

        return JsonResponse(data)