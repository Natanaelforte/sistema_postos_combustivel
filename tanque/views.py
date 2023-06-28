from django.urls import reverse, reverse_lazy
import requests

from base.views import CreateBaseView, ListBaseView, UpdateBaseView, DeleteBaseView, TableBaseView, ActionBaseView
from combustivel.choices.choices_combustivel import C_TIPO_DE_COMBUSTIVEL
from tanque.forms import TanqueForm
from tanque.models import Tanque


class TanqueListView(ListBaseView):
    model = Tanque
    template_name = 'tanque/list.html'


class TanqueTableView(TableBaseView):
    model = Tanque
    search_fields = [('combustivel__tipo_de_combustivel', C_TIPO_DE_COMBUSTIVEL)]
    template_name = 'tanque/table.html'


class TanqueCreateView(CreateBaseView):
    model = Tanque
    template_name = 'tanque/forms.html'
    form_class = TanqueForm

    def get_success_url(self):
        return reverse('tanque:list')


class TanqueUpdateView(UpdateBaseView):
    model = Tanque
    template_name = 'tanque/update.html'
    form_class = TanqueForm

    def get_success_url(self):
        return reverse('tanque:list')


class TanqueDeleteView(DeleteBaseView):
    model = Tanque
    template_name = 'tanque/delete.html'
    success_url = reverse_lazy("tanque:list")


class PrecoUnitario(ActionBaseView):
    template_name = 'tanque/preco_unitario.html'

    def get_payload(self, url, payload):
        url = ""

        payload = ''
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ASPSESSIONIDASDCBTRA=GINMMEEBHFIENPHHIHOEBBKD'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            response = self.get_payload(url='URL', payload='payloads')
            data['resposta'] = 'sim'
            data['preco'] = response
        except Exception as e:
            data['resposta'] = 'não'
            data['mensagem'] = str(e)

            """mostrar mensagem de erro 'Erro ao tentar salvar {str(e)}' e a resposta não"""

        return data