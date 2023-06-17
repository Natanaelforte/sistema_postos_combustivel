from posto.models import Posto


class PostoMixin:
    def _get_instance_posto(self):
        if hasattr(self, 'request'):
            request = getattr(self, 'request')

            return Posto.objects.get(pk=request.session['posto_pk'])

        elif hasattr(self, 'object') and hasattr(self.object, 'posto'):
            return self.object.posto

        return None


class PostoUsuarioContextMixin(PostoMixin):

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        posto = self._get_instance_posto()

        context_data.update({'posto': posto, 'usuario': self.request.user})

        return context_data
