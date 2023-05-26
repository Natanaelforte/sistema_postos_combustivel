# Generated by Django 4.2.1 on 2023-05-25 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('combustivel', '0004_alter_combustivel_tipo_de_combustivel'),
        ('virgencia_de_preco', '0003_rename_vigencia_de_preco_vigenciadepreco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vigenciadepreco',
            name='combustivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precoVigente', to='combustivel.combustivel', verbose_name='Combustivel'),
        ),
    ]