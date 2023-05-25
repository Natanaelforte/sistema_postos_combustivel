from django.db import models

from bomba_de_combustivel.models import Bomba
from combustivel.models import Combustivel
from colaborador.models import Colaborador


class Abastecimento(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True, blank=True)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    combustivel = models.ForeignKey(Combustivel, on_delete=models.CASCADE)
    litros_abastecido = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    valor_total = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    data = models.DateTimeField('Data do abastecimento')

    def __str__(self):
        return f'Abastecido por, {self.colaborador}, na {self.bomba} as {self.data.strftime("%H:%M:%S, %d/%m/%Y")}.'

    class Meta:
        db_table = 'Abastecimento'
        verbose_name = 'Abastecimento'
        verbose_name_plural = 'Abastecimentos'
        ordering = []
