# Generated by Django 4.1 on 2022-09-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudrh', '0006_remove_candidatos_principales_capacitaciones_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleados',
            old_name='candidatos',
            new_name='candidato',
        ),
        migrations.RemoveField(
            model_name='candidatos',
            name='experiencia_laboral',
        ),
        migrations.AddField(
            model_name='candidatos',
            name='experiencia_laboral',
            field=models.ManyToManyField(to='crudrh.experiencia_laboral'),
        ),
    ]