# Generated by Django 4.1.7 on 2023-05-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_planta_imagens_planta_imagens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='planta',
        ),
        migrations.AddField(
            model_name='planta',
            name='descricao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
