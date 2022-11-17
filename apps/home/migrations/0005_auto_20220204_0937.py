# Generated by Django 2.2.5 on 2022-02-04 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20220204_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucion',
            name='id_modalidad',
        ),
        migrations.CreateModel(
            name='DetalleModalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_grabacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Institucion', verbose_name='Institucion perteneciente')),
                ('id_modalidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Modalidad', verbose_name='MOdalidad')),
                ('usuario_grabacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usuario_grabacion_detallemodalidad', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usuario_modificacion_detallemodalidad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Modalidades de Mined',
            },
        ),
    ]
