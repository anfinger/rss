# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reisen', '0002_auto_20151230_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='reise',
            name='untertitel',
            field=models.CharField(default=b'', max_length=1024),
        ),
    ]
