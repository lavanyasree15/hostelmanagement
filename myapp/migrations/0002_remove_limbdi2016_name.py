# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-02 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='limbdi2016',
            name='name',
        ),
    ]
