# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 04:27
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('elos', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('elo_changes', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
        ),
    ]
