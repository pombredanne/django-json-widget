# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 17:13
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
