from django.contrib.auth.models import AbstractUser
from posto.models import Posto
from django.db import models


class Usuario(AbstractUser):
    posto = models.ManyToManyField(Posto, verbose_name='Posto', related_name='usuario')

    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    # def __str__(self):
    #     return f'{self.nome} / {self.funcao}'