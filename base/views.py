from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

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


class DeleteBaseView(PostoUsuarioContextMixin, DeleteView):
    pass


class TableBaseView(ListBaseView):
    search_fields = None

    def get_value(self, search, search_field):
        if len(search_field) > 1 and type(search_field[1]) == list:
            for c in search_field[1]:
                if search in c[1]:
                    return c[0]

        return search

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = super().get_queryset()

        if self.search_fields and search:
            kwwargs_search = {}

            for search_field in self.search_fields:
                kwwargs_search[f'{search_field[0]}__icontains'] = self.get_value(search, search_field)

            queryset = queryset.filter(**kwwargs_search)

        return queryset

    def get(self, request, *args, **kwargs):
        resutado = super().get(request, *args, **kwargs)

        return JsonResponse({'tabela': resutado.rendered_content})