# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew_data', '0008_auto_20171030_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='fermentabletype',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
