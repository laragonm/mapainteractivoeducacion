# Generated by Django 2.2.5 on 2022-02-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20220219_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='codigoestablecimiento',
            field=models.CharField(blank=True, max_length=10, verbose_name='Codigo Establecimiento/ MINED'),
        ),
    ]