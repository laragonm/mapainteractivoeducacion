# Generated by Django 2.2.5 on 2022-02-17 20:09

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20220216_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPatrimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_patrimonio', models.ImageField(blank=True, upload_to=apps.home.models.imagenbannerPatrimonio_path, verbose_name='Banner Principal Patrimonio')),
            ],
            options={
                'verbose_name': 'Logo Gobierno',
            },
        ),
        migrations.AlterField(
            model_name='institucion',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'CENTRO TECNOLÓGICO - INATEC'), (2, 'CENTRO TECNOLÓGICO ACREDITADO - INATEC'), (3, 'CENTRO ESCOLAR - PUBLICO'), (4, 'ESCUELA NORMAL - PUBLICA'), (5, 'UNIVERSIDAD LEGALMENTE CONSTITUIDA'), (6, 'UNIVERSIDAD MIEMBRO'), (7, 'CENTRO ESCOLAR - PRIVADO'), (8, 'ESCUELA NORMAL - PRIVADA')], default=1, verbose_name='Tipo Institucion'),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'CENTRO TECNOLÓGICO - INATEC'), (2, 'CENTRO TECNOLÓGICO ACREDITADO - INATEC'), (3, 'CENTRO ESCOLAR - PUBLICO'), (4, 'ESCUELA NORMAL - PUBLICA'), (5, 'UNIVERSIDAD LEGALMENTE CONSTITUIDA'), (6, 'UNIVERSIDAD MIEMBRO'), (7, 'CENTRO ESCOLAR - PRIVADO'), (8, 'ESCUELA NORMAL - PRIVADA')], default=1, verbose_name='Tipo Institucion'),
        ),
    ]