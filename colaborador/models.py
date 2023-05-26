from django.db import models
from funcao.models import Funcao
from posto.models import Posto


class Colaborador(models.Model):
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Posto')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(max_length=100, verbose_name='CPF')
    contato = models.CharField(max_length=100, verbose_name='Contato')
    endereco = models.CharField(max_length=300, verbose_name='Endereço')
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, verbose_name='Função')

    def __str__(self):
        return f'{self.nome} / {self.funcao}'

    class Meta:
        db_table = 'Colaborador'
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
