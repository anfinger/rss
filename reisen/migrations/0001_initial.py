# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reise',
            fields=[
                ('reiseID', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('titel', models.CharField(max_length=256)),
                ('einleitung', models.TextField()),
                ('reiselink', models.URLField()),
                ('datum_erzeugung', models.DateTimeField(default=django.utils.timezone.now)),
                ('datum_veroeffentlichung', models.DateTimeField(null=True, blank=True)),
                ('datum_beginn', models.DateField(null=True, blank=True)),
                ('datum_ende', models.DateField(null=True, blank=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reisetage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagnummer', models.IntegerField()),
                ('reise', models.ForeignKey(to='reisen.Reise')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagID', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('beschreibung', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='reisetage',
            name='tag',
            field=models.ForeignKey(to='reisen.Tag'),
        ),
        migrations.AddField(
            model_name='reise',
            name='tage',
            field=models.ManyToManyField(to='reisen.Tag', through='reisen.Reisetage'),
        ),
    ]
