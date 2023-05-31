from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView

from base.views import CreateBaseView, ListBaseView
from .forms import ColaboradorForm
from .models import Colaborador


class ColaboradorListView(ListBaseView):
    model = Colaborador
    template_name = 'colaborador/list.html'


class ColaboradorCreateView(CreateBaseView):
    model = Colaborador
    template_name = 'colaborador/form.html'
    form_class = ColaboradorForm

    def get_success_url(self):
        return reverse('colaborador:list')


class ColaboradorUpdateView(UpdateView):
    model = Colaborador
    fields = ['nome', 'cpf', 'contato', 'endereco', 'funcao']
    template_name = 'colaborador/update.html'

    def get_success_url(self):
        return reverse('colaborador:list')


class ColaboradorDeleteView(DeleteView):
    model = Colaborador
    template_name = 'colaborador/delete.html'
    success_url = reverse_lazy("colaborador:list")

# def colaborador_json(request):
#     username = request.GET.get('username', None)
#
#     if not username:
#         HttpResponse({}, content_type="application/json")
#
#     colaborador_json_response = Colaborador.objects.filter(usuario__username=username)
#
#     data = serialize("json", colaborador_json_response, fields=('posto', 'nome', 'funcao', 'id'))
#
#     return HttpResponse(data, content_type="application/json")
