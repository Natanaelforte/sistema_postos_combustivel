from django.db import models

from bomba_de_combustivel.models import Bomba
from combustivel.models import Combustivel
from colaborador.models import Colaborador
from posto.models import Posto


class Abastecimento(models.Model):
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posto')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True, blank=True)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    combustivel = models.ForeignKey(Combustivel, on_delete=models.CASCADE)
    litros_abastecido = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    data = models.DateTimeField('Data do abastecimento')

    class Meta:
        db_table = 'Abastecimento'
        verbose_name = 'Abastecimento'
        verbose_name_plural = 'Abastecimentos'

    def __str__(self):
        return f'Abastecido por, {self.colaborador}, na {self.bomba} as {self.data.strftime("%H:%M:%S, %d/%m/%Y")}.'

    @property
    def valor_total(self):
        valor_vigente = self.combustivel.valor_vigente
        litros = self.litros_abastecido
        valor = valor_vigente.valor * litros
        return valor
