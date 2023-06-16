from django.db import models
from posto.models import Posto


class Funcao(models.Model):
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, verbose_name='Posto')
    codigo = models.CharField(max_length=500, verbose_name='Código')
    descricao = models.CharField(max_length=600, verbose_name='Descrição')


    class Meta:
        db_table = 'Função'
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'

    def __str__(self):
        return self.descricao
