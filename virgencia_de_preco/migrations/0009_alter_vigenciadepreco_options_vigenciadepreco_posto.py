# Generated by Django 4.2.1 on 2023-05-26 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0002_alter_posto_options'),
        ('virgencia_de_preco', '0008_remove_vigenciadepreco_data_de_vigencia_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vigenciadepreco',
            options={'verbose_name': 'Vigência de preço', 'verbose_name_plural': 'Vigência de preços'},
        ),
        migrations.AddField(
            model_name='vigenciadepreco',
            name='posto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posto.posto', verbose_name='Posto'),
        ),
    ]