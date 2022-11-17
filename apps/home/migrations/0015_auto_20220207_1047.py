# Generated by Django 2.2.5 on 2022-02-07 16:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220207_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, max_length=200, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'INATEC'), (2, 'CENTRO ESCOLAR'), (3, 'ESCUELA NORMAL'), (4, 'UNIVERSIDAD ESTABLECIDA'), (5, 'UNIVERSIDAD MIEMBRO'), (6, 'CENTRO PRIVADO - INATEC')], default=1, verbose_name='Tipo Institucion'),
        ),
    ]
