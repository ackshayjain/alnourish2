# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('volume', models.IntegerField()),
                ('test_date', models.CharField(max_length=200, default='')),
                ('ph_test', models.CharField(max_length=200, default='')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2018, 4, 29, 21, 7, 24, 136840))),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
