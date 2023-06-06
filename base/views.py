from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView

from base.mixins import PostoUsuarioContextMixin
from posto.models import Posto


class CreateBaseView(PostoUsuarioContextMixin, CreateView):
    def _get_posto(self):
        return get_object_or_404(Posto, pk=self.request.session['posto_pk'])

    def form_valid(self, form):
        form.instance.posto = self._get_posto()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'posto_pk': self.request.session['posto_pk']})

        return kwargs


class ListBaseView(PostoUsuarioContextMixin, ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(posto__pk=self.request.session['posto_pk'])
        return queryset


class UpdateBaseView(PostoUsuarioContextMixin, UpdateView):

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'posto_pk': self.request.session['posto_pk']})

        return kwargs
