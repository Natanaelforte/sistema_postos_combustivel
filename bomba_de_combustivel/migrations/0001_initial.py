# Generated by Django 4.2.1 on 2023-05-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tanque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_bomba', models.IntegerField(blank=True, null=True)),
                ('tanques', models.ManyToManyField(to='tanque.tanque')),
            ],
            options={
                'verbose_name': 'Bomba de Combustível',
                'verbose_name_plural': 'Bombas de Combustível',
                'db_table': 'Bomba de Combustível',
                'ordering': [],
            },
        ),
    ]
