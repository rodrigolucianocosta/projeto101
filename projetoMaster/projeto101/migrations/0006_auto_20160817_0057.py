# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto101', '0005_auto_20160817_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projeto101.Medico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projeto101.Paciente'),
            preserve_default=False,
        ),
    ]
