# Generated by Django 2.2.5 on 2022-02-16 15:11

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20220215_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_actual', models.ImageField(blank=True, upload_to=apps.home.models.imagenDepartamento_path, verbose_name='Imagen Logo Actual')),
            ],
            options={
                'verbose_name': 'Logo Gobierno',
            },
        ),
        migrations.AddField(
            model_name='subsistema',
            name='imagen_cp',
            field=models.ImageField(blank=True, null=True, upload_to=apps.home.models.imagenInstituciones_path, verbose_name='Imagen Default Tarjeta - Centro Pivado/INATEC'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='sector',
            field=models.CharField(blank=True, choices=[('2', 'Agropecuario y Forestal'), ('3', 'Industria y Construccion'), ('4', 'Comercio y Servicio')], max_length=10, verbose_name='Sector - Inatec'),
        ),
    ]
