# Generated by Django 4.1.7 on 2023-04-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='data_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='obras',
            name='data_prevista',
            field=models.DateField(),
        ),
    ]
