from django.db import models
from tanque.models import Tanque


class Bomba(models.Model):
    numero_bomba = models.IntegerField(null=True, blank=True)
    tanques = models.ManyToManyField('tanque.Tanque')

    def __str__(self):
        return f'Bomba {self.numero_bomba}'

    class Meta:
        db_table = 'Bomba de Combustível'
        verbose_name = 'Bomba de Combustível'
        verbose_name_plural = 'Bombas de Combustível'
        ordering = []
