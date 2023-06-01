from posto.models import Posto


class PostoMixin:
    def _get_instance_posto(self):
        if hasattr(self, 'request'):
            request = getattr(self, 'request')

            return Posto.objects.get(pk=request.session['posto_pk'])

        elif hasattr(self, 'object') and hasattr(self.object, 'posto'):
            return self.object.posto

        return None
