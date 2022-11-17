# Generated by Django 2.2.5 on 2022-02-09 22:39

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20220209_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=apps.home.models.imagenEvento_path, verbose_name='Imagen de evento'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=apps.home.models.imagenNoticia_path, verbose_name='Imagen de noticia'),
        ),
        migrations.AlterField(
            model_name='subsistema',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=apps.home.models.imagenInstituciones_path, verbose_name='Imagen Default Tarjeta'),
        ),
        migrations.AlterField(
            model_name='subsistema',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to=apps.home.models.imagenSubsistema_path, verbose_name='Imagen Portada'),
        ),
    ]