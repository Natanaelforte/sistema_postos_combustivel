from django.db import models


class Posto(models.Model):
    razao_social = models.CharField(verbose_name='Razão Social', max_length=100)
    cnpj = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    endereco = models.CharField(verbose_name='Endereço',max_length=300)

    class Meta:
        db_table = 'Posto'
        verbose_name = 'Posto de Combustível'
        verbose_name_plural = 'Postos de Combustível'

    def __str__(self):
        return f'{self.razao_social} / {self.cnpj}'
