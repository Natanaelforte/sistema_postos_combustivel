from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from base.mixins import PostoMixin


class DashboardView(generic.TemplateView, PostoMixin, LoginRequiredMixin):
    template_name = 'inicio/dashboard.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        posto = self._get_instance_posto()

        context_data.update({'posto': posto, 'usuario': self.request.user})

        return context_data
