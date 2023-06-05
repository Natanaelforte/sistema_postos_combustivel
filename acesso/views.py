from django.contrib.auth.views import LoginView
from django.urls import reverse

from acesso.forms import AcessoForm


class AcessoLoginView(LoginView):
    template_name = 'acesso/login.html'
    form_class = AcessoForm

    def get_success_url(self):
        return reverse('inicio:dashboard')

    def form_valid(self, form):
        self.request.session['posto_pk'] = self.request.POST.get('posto', None)

        return super(AcessoLoginView, self).form_valid(form)


