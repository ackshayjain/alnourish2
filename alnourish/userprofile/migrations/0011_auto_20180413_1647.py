# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20180413_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 16, 47, 15, 800666)),
        ),
    ]