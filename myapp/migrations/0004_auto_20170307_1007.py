# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-07 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170305_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': False, 'ordering': ('roll_no',)},
        ),
    ]
