from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Posto


def posto_json(request):
    username = request.GET.get('username', None)

    if not username:
        HttpResponse({}, content_type="application/json")

    posto_json_response = Posto.objects.filter(usuario__username=username)

    data = serialize("json", posto_json_response, fields=('razao_social', 'cnpj', 'id'))

    return HttpResponse(data, content_type="application/json")
