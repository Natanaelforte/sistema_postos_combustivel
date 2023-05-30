from django.urls import reverse
from django.views.generic import ListView, CreateView

from abastecimento.forms import AbastecimentoForm
from abastecimento.models import Abastecimento


class AbastecimentoListViewl(ListView):
    model = Abastecimento
    template_name = 'abastecimento/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset


class AbastecimentoCreate(CreateView):
    model = Abastecimento
    template_name = 'abastecimento/forms.html'
    form_class = AbastecimentoForm

    def get_success_url(self):
        return reverse('abastecimento:abastecimento_list')
