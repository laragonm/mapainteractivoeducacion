# Generated by Django 2.2.5 on 2022-02-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20220214_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='sector',
            field=models.CharField(blank=True, choices=[(2, 'Agropecuario y Forestal'), (3, 'Industria y Construccion'), (4, 'Comercio y Servicio')], max_length=50, verbose_name='Sector - Inatec'),
        ),
    ]
