from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from base.views import CreateBaseView, ListBaseView, UpdateBaseView
from tanque.forms import TanqueForm
from tanque.models import Tanque


class TanqueListView(ListBaseView):
    model = Tanque
    template_name = 'tanque/list.html'


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


class TanqueDeleteView(DeleteView):
    model = Tanque
    template_name = 'tanque/delete.html'
    success_url = reverse_lazy("tanque:list")
