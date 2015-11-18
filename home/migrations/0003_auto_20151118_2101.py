# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151118_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktuelles',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktuelles',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
