# Generated by Django 5.0.6 on 2024-05-11 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_diassemana_horario_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': 'Professor', 'verbose_name_plural': 'Professores'},
        ),
    ]