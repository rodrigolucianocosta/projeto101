# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-20 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto101', '0010_pessoa_data_nascimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='prontuario',
        ),
        migrations.AddField(
            model_name='paciente',
            name='cartao_sus',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]