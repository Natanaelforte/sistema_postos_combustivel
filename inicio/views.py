from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'inicio/dashboard.html'
