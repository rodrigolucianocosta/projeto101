# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto101', '0004_auto_20160817_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto101.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto101.Paciente'),
        ),
    ]