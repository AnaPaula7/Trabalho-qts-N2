# Generated by Django 5.0.6 on 2024-05-11 14:56

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_diassemana_horario_fim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diassemana',
            name='horario',
            field=models.TimeField(verbose_name='Horario do Inicio'),
        ),
        migrations.AlterField(
            model_name='diassemana',
            name='horario_fim',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='Horario que termina'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='professor', variations={'thumb': {'crop': True, 'height': 200, 'width': 200}}, verbose_name='Imagem'),
        ),
    ]