# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-27 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180327_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
    ]
