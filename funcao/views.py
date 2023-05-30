from django.urls import reverse
from django.views.generic import ListView, CreateView

from funcao.forms import FuncaoForm
from funcao.models import Funcao


class FuncaoListViewl(ListView):
    model = Funcao
    template_name = 'funcao/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset


class FuncaoCreate(CreateView):
    model = Funcao
    template_name = 'funcao/forms.html'
    form_class = FuncaoForm

    def get_success_url(self):
        return reverse('funcao:funcao_list')
