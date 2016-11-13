# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-13 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proyeccion', '0004_auto_20161015_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('director_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.Docente')),
                ('facultad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField()),
                ('informacion_descriptiva_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.InformacionDescriptiva')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_horas_semana', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('tipo_financiacion', models.CharField(max_length=200)),
                ('docente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.Docente')),
                ('proyecto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('codigo', models.CharField(max_length=200)),
                ('semestre', models.IntegerField(null=True)),
                ('numero_horas_semana', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('programa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.Programa')),
                ('proyecto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyeccion.Proyecto')),
            ],
        ),
    ]
