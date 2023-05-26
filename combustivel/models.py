from django.db import models
from datetime import datetime
from combustivel.choices.choices_combustivel import C_TIPO_DE_COMBUSTIVEL, GASOLINA
from posto.models import Posto


class Combustivel(models.Model):
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posto')
    tipo_de_combustivel = models.IntegerField(choices=C_TIPO_DE_COMBUSTIVEL, default=GASOLINA)

    class Meta:
        db_table = 'Combustivel'
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'

    def __str__(self):
        return f'{self.get_tipo_de_combustivel_display()} / {self.posto}'

    @property
    def valor_vigente(self):
        vigencias_de_precos = self.vigencias_de_precos.objects.filter(
            data_de_inicio__gte=datetime.now(), data_de_termino__lte=datetime.now(), ativo=True
        )

        if vigencias_de_precos.exists():
            return vigencias_de_precos.first().valor

        return 0
