# Generated by Django 5.0.6 on 2024-05-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_disponibilidade_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='disponibilidade',
            field=models.ManyToManyField(related_name='professores', to='core.diassemana', verbose_name='Disponibilidade'),
        ),
        migrations.DeleteModel(
            name='Disponibilidade',
        ),
    ]
