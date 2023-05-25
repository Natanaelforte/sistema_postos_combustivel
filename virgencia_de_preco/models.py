from django.db import models
from combustivel.models import Combustivel


class VigenciaDePreco(models.Model):
    combustivel = models.ForeignKey(
        Combustivel, on_delete=models.CASCADE, related_name='vigencias_de_precos', verbose_name='Combustivel',
        blank=True, null=True
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    data_de_inicio = models.DateField(verbose_name='Data de Início', null=True, blank=True)
    data_de_termino = models.DateField(verbose_name='Data de Término', null=True, blank=True)
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        db_table = 'Vigencia_de_preco'
        verbose_name = 'Vigência de preço'
        verbose_name_plural = 'Vigência de preços'
        ordering = []

    def __str__(self):
        return f'{self.combustivel} / {self.ativo_display}'

    @property
    def ativo_display(self):
        if self.ativo:
            return 'Ativo'

        return 'Inativo'
