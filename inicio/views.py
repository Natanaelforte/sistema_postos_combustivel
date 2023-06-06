from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from base.mixins import  PostoUsuarioContextMixin


class DashboardView(PostoUsuarioContextMixin, generic.TemplateView, LoginRequiredMixin):
    template_name = 'inicio/dashboard.html'


