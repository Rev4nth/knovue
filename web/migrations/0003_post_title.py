# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170309_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]