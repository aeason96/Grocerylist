# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20171021_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='grocerylist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Grocerylist'),
            preserve_default=False,
        ),
    ]
