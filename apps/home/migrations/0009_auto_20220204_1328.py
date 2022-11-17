# Generated by Django 2.2.5 on 2022-02-04 19:28

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220204_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videohome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to=apps.home.models.Video_path, verbose_name='Video Presentacion')),
            ],
            options={
                'verbose_name': 'Video Presentacion',
            },
        ),
        migrations.AlterField(
            model_name='evento',
            name='link',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='link del Evento'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'INATEC'), (2, 'CENTRO'), (3, 'ESCUELA NORMAL'), (4, 'UNIVERSIDAD ESTABLECIDA'), (5, 'UNIVERSIDAD MIEMBRO')], default=1, verbose_name='Tipo Institucion'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='web',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='Sitio web'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='link',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='link del Noticia'),
        ),
        migrations.AlterField(
            model_name='subsistema',
            name='web',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='Sitio web'),
        ),
    ]
