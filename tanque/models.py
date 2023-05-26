from django.db import models
from combustivel.models import Combustivel
from posto.models import Posto


class Tanque(models.Model):
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posto')
    combustivel = models.ForeignKey(Combustivel, on_delete=models.CASCADE)
    quantidade_litros = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'Tanque'
        verbose_name = 'Tanque de Combustível'
        verbose_name_plural = 'Tanques de Combustível'

    def __str__(self):
        return f'Tanque / {self.combustivel} / {self.posto}'
