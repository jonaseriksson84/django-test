# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='last_rented',
            field=models.DateTimeField(blank=True),
        ),
    ]
