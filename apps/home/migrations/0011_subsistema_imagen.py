# Generated by Django 2.2.5 on 2022-02-05 02:41

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220204_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsistema',
            name='imagen',
            field=models.ImageField(default=0.0004945598417408506, upload_to=apps.home.models.imagenInstituciones_path, verbose_name='Imagen default'),
            preserve_default=False,
        ),
    ]
