from django.core.serializers import serialize
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView

from .forms import ColaboradorForm
from .models import Colaborador
from django.views.generic.list import ListView


class ColaboradorListViewl(ListView):
    model = Colaborador
    template_name = 'colaborador/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset


class ColaboradorCreate(CreateView):
    model = Colaborador
    template_name = 'colaborador/form.html'
    form_class = ColaboradorForm

    def get_success_url(self):
        return reverse('colaborador:colaborador_list')

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
