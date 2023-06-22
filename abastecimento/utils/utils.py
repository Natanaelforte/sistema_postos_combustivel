def _try_get_param(self, param_name):
    try:
        if param_name:
            parametro = self.request.GET.get(param_name)

            if parametro and parametro == 'null':
                return None

            return parametro
        else:
            return None
    except:
        pass


def _try_get_instance(class_name, pk):
    try:
        instance = class_name.objects.get(pk=pk)
        return instance
    except:
        instance = None
        return instance