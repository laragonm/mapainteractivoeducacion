# Generated by Django 2.2.5 on 2022-02-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220207_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'INATEC'), (2, 'CENTRO PRIVADO - INATEC'), (3, 'CENTRO ESCOLAR'), (4, 'ESCUELA NORMAL'), (5, 'UNIVERSIDAD ESTABLECIDA'), (6, 'UNIVERSIDAD MIEMBRO')], default=1, verbose_name='Tipo Institucion'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'INATEC'), (2, 'CENTRO PRIVADO - INATEC'), (3, 'CENTRO ESCOLAR'), (4, 'ESCUELA NORMAL'), (5, 'UNIVERSIDAD ESTABLECIDA'), (6, 'UNIVERSIDAD MIEMBRO')], default=1, verbose_name='Tipo Institucion'),
        ),
    ]
