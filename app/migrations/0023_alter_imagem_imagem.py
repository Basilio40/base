# Generated by Django 4.1.7 on 2023-08-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_img1_imagem_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.FileField(default=1, upload_to='img'),
            preserve_default=False,
        ),
    ]
