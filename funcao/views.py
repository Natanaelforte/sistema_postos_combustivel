from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from base.views import CreateBaseView, ListBaseView, UpdateBaseView
from funcao.forms import FuncaoForm
from funcao.models import Funcao


class FuncaoListView(ListBaseView):
    model = Funcao
    template_name = 'funcao/list.html'


class FuncaoCreateView(CreateBaseView):
    model = Funcao
    template_name = 'funcao/forms.html'
    form_class = FuncaoForm

    def get_success_url(self):
        return reverse('funcao:list')


class FuncaoUpdateView(UpdateBaseView):
    model = Funcao
    fields = ['codigo', 'descricao']
    template_name = 'funcao/update.html'

    def get_success_url(self):
        return reverse('funcao:list')


class FuncaoDeleteView(DeleteView):
    model = Funcao
    template_name = 'funcao/delete.html'
    success_url = reverse_lazy("funcao:list")
