# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-28 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Rejected',
            field=models.BooleanField(default=False),
        ),
    ]
