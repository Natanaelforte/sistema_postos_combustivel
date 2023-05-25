from django.db import models


class Vigencia_de_preco(models.Model):
    combustivel = models.CharField(max_length=100, verbose_name='Combustivel')
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    data_de_vigencia = models.DateField(verbose_name='Data de Vigência')
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
