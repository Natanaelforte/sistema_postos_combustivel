from django.db import models

from posto.models import Posto
from tanque.models import Tanque


class Bomba(models.Model):
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posto')
    numero = models.IntegerField(null=True, blank=True)
    tanques = models.ManyToManyField('tanque.Tanque')

    def __str__(self):
        return f'Bomba {self.numero}'

    class Meta:
        db_table = 'Bomba de Combustível'
        verbose_name = 'Bomba de Combustível'
        verbose_name_plural = 'Bombas de Combustível'

