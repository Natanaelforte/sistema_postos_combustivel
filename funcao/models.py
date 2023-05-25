from django.db import models
from posto.models import Posto


class Funcao(models.Model):
    codigo = models.CharField(max_length=500, verbose_name='Código')
    descricao = models.CharField(max_length=600, verbose_name='Descrição')
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, verbose_name='Posto')

    def __str__(self):
        return f'{self.descricao}'

    class Meta:
        db_table = 'Função'
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'
        ordering = []
