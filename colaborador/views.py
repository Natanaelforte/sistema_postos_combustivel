from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Colaborador
from django.views.generic.list import ListView


class ColaboradorListViewl(ListView):
    model = Colaborador
    template_name = 'colaborador/colaborador_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset






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
