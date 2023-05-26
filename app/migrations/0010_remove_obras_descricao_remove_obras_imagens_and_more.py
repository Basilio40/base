# Generated by Django 4.1.7 on 2023-05-25 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_obras_adm_remove_obras_layout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obras',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='imagens',
        ),
        migrations.RemoveField(
            model_name='obras',
            name='planta_data',
        ),
        migrations.CreateModel(
            name='Arquitetonico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('planta_data', models.DateField(blank=True, null=True)),
                ('imagens', models.FileField(upload_to='planta')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.obras')),
            ],
        ),
    ]
