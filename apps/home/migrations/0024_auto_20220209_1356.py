# Generated by Django 2.2.5 on 2022-02-09 19:56

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20220209_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='edad_12a18',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='edad_18',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='edad_3a5',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='edad_6a11',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_e',
            field=models.PositiveSmallIntegerField(blank=True, default=-2022, verbose_name='Cantidad de estudiantes Especial /Mined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_f',
            field=models.PositiveSmallIntegerField(blank=True, default=2, verbose_name='Cantidad de estudiantes Formacion Docente /Mined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_i',
            field=models.PositiveSmallIntegerField(blank=True, default=-2022, verbose_name='Cantidad de estudiantes Inicial /Mined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_p',
            field=models.PositiveSmallIntegerField(blank=True, default=-2022, verbose_name='Cantidad de estudiantes Primaria /Mined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_s',
            field=models.PositiveSmallIntegerField(blank=True, default=2, verbose_name='Cantidad de estudiantes Secundaria /Mined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_t',
            field=models.PositiveSmallIntegerField(blank=True, default=-2022, verbose_name='Cantidad de estudiantes Bachiller Tecnico /Inatec'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_te',
            field=models.PositiveSmallIntegerField(blank=True, default=-2022, verbose_name='Cantidad de estudiantes Tecnico Especialista /Inatec'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_tg',
            field=models.PositiveSmallIntegerField(blank=True, default=0.0004945598417408506, verbose_name='Cantidad de estudiantes Tecnico General /Inatec'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='estudiantes_ts',
            field=models.PositiveSmallIntegerField(blank=True, default=0.0004945598417408506, verbose_name='Cantidad de estudiantes Tecnico Superior /Inatec'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subsistema',
            name='imagen',
            field=models.ImageField(upload_to=apps.home.models.imagenInstituciones_path, verbose_name='Imagen Default Tarjeta'),
        ),
    ]
