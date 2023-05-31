from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView

from posto.models import Posto


class CreateBaseView(CreateView):
    def _get_posto(self):
        return get_object_or_404(Posto, pk=self.request.session['posto'])

    def form_valid(self, form):
        form.instance.posto = self._get_posto()
        return super().form_valid(form)


class ListBaseView(ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto'])
        return queryset
