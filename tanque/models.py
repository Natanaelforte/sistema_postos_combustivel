from django.db import models
from combustivel.models import Combustivel


class Tanque(models.Model):
    combustivel = models.ForeignKey(Combustivel, on_delete=models.CASCADE)
    quantidade_litros = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'Tanque / {self.combustivel}'

    class Meta:
        db_table = 'Tanque'
        verbose_name = 'Tanque de Combustível'
        verbose_name_plural = 'Tanques de Combustível'
        ordering = []

    # @property
    # def valo(self):
