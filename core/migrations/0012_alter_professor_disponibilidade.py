# Generated by Django 5.0.6 on 2024-05-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_professor_disponibilidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='disponibilidade',
            field=models.ManyToManyField(blank=True, default=None, to='core.diassemana', verbose_name='Disponibilidade'),
        ),
    ]