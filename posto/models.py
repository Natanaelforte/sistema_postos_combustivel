from django.db import models


class Posto(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.IntegerField(max_length=100)
    contato = models.IntegerField(max_length=100)
    endereco = models.CharField(max_length=300)