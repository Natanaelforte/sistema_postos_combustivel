from django.db import models
from combustivel.choices.choices_combustivel import tipo_de_combustivel_choice


class Combustivel(models.Model):
    tipo_de_combustivel = models.CharField(max_length=20, choices=tipo_de_combustivel_choice, default=None)

    class Meta:
        db_table = 'Combustivel'
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'
        ordering = []

    def __str__(self):
        return self.tipo_de_combustivel

    @property
    def valor_vigente(self):
        vigencias_de_precos = self.vigencias_de_precos.filter()

        if vigencias_de_precos.exists():
            return vigencias_de_precos.first()
