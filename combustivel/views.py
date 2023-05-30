from django.urls import reverse
from django.views.generic import ListView, CreateView

from combustivel.forms import CombustivelForm
from combustivel.models import Combustivel


class CombustivelListViewl(ListView):
    model = Combustivel
    template_name = 'combustivel/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset


class CombustivelCreate(CreateView):
    model = Combustivel
    template_name = 'combustivel/forms.html'
    form_class = CombustivelForm

    def get_success_url(self):
        return reverse('combustivel:combustivel_list')
