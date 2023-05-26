from django.contrib.auth.views import LoginView
from django.urls import reverse


class AcessoLoginView(LoginView):
    template_name = 'acesso/login.html'

    def get_success_url(self):
        return reverse('inicio:dashboard')
