from django.urls import reverse
from django.views.generic import ListView, CreateView

from .forms import BombaForm
from .models import Bomba


class BombaListViewl(ListView):
    model = Bomba
    template_name = 'bomba_de_combustivel/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset


class BombaCreate(CreateView):
    model = Bomba
    template_name = 'bomba_de_combustivel/forms.html'
    form_class = BombaForm

    def get_success_url(self):
        return reverse('bomba_de_combustivel:bomba')
