# Generated by Django 5.0.6 on 2024-05-18 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_disciplina_professor_delete_disciplinaprofessor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplina',
            options={'verbose_name': 'Disciplina', 'verbose_name_plural': 'Disciplinas'},
        ),
    ]
