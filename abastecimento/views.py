from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView
import pydf

from abastecimento.forms import AbastecimentoForm
from abastecimento.models import Abastecimento
from base.views import ListBaseView, UpdateBaseView, ActionBaseView, TableBaseView
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


class AbastecimentoRelatorioPdf(TableBaseView):
    model = Abastecimento
    template_name = 'abastecimento/relatorio_pdf/body.html'

    def _try_get_param(self, param_name):
        try:
            if param_name:
                parametro = self.request.GET.get(param_name)

                if parametro and parametro == 'null':
                    return None

                return parametro
            else:
                return None
        except:
            pass

    def _try_get_instance(self, class_name, pk):
        try:
            instance = class_name.objects.get(pk=pk)
            return instance
        except:
            instance = None
            return instance

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

    def calculo_total_valor(self):
        abastecimentos = self.get_queryset()
        total_valor = float(0)

        if abastecimentos.exists():
            for abastecimento in abastecimentos:
                total_valor += float(abastecimento.calculate_valor_total())

        return f'R$ {total_valor:.2f}'


    def calculo_total_litros(self):
        abastecimentos = self.get_queryset()
        total_litros = float(0)

        if abastecimentos.exists():
            for abastecimento in abastecimentos:
                total_litros += float(abastecimento.litros_abastecido)

        return f' {total_litros:.2f}'


    def get_response(self, context):

        html = render_to_string(self.template_name, context)

        html_header_str = render_to_string('abastecimento/relatorio_pdf/header.html', context)
        html_header_file = pydf.NamedTemporaryFile(suffix='.html')
        html_header_file.write(html_header_str.encode('utf8'))
        html_header_file.seek(0)

        html_footer_str = render_to_string('abastecimento/relatorio_pdf/footer.html', context)
        html_footer_file = pydf.NamedTemporaryFile(suffix='.html')
        html_footer_file.write(html_footer_str.encode('utf8'))
        html_footer_file.seek(0)

        report_pdf = pydf.generate_pdf(html,
                                       page_size='A4',
                                       orientation='portrait',
                                       margin_left='20mm',
                                       margin_right='5mm',
                                       header_html=html_header_file.name,
                                       footer_html=html_footer_file.name,
                                       )

        response = HttpResponse(report_pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="relatório-abastecimento.pdf"'

        return response

    def context_create(self):

        quetyset = self.get_queryset()

        bomba_id = self._try_get_param('bomba')
        combustivel_id = self._try_get_param('combustivel')
        colaborador_id = self._try_get_param('colaborador')

        bomba = self._try_get_instance(Bomba, bomba_id)
        combustivel = self._try_get_instance(Combustivel, combustivel_id)
        colaborador = self._try_get_instance(Colaborador, colaborador_id)

        context = {
            'bomba': bomba,
            'combustivel': combustivel,
            'colaborador': colaborador,
            'abastecimentos': quetyset,
            'total_litros': self.calculo_total_litros(),
            'total_valor': self.calculo_total_valor()
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.context_create()

        return self.get_response(context)
