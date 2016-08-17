# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=60)),
            ],
        ),
    ]
