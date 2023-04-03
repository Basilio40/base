# Generated by Django 4.1.7 on 2023-04-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=25)),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=255)),
                ('data_inicio', models.DateTimeField()),
                ('data_prevista', models.DateTimeField()),
                ('imagens', models.ManyToManyField(to='app.imagem')),
            ],
        ),
    ]