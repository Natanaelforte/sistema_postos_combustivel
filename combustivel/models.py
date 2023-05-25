from django.db import models


class Combustivel(models.Model):
    gasolina = 'Gasolina'
    disel = 'Disel'
    tipo_de_combustivel_choice = [
        (gasolina, 'Gasolina'),
        (disel, 'Disel')
    ]

    tipo_de_combustivel = models.CharField(
        max_length=20, choices=tipo_de_combustivel_choice, default=gasolina
    )
    valor = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.tipo_de_combustivel

    class Meta:
        db_table = 'Combustivel'
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'
        ordering = []
