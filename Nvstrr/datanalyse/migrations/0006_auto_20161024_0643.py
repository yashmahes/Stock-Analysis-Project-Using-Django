# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datanalyse', '0005_delete_monthlyweatherbycity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userports',
            name='boughtat',
            field=models.FloatField(),
        ),
    ]
