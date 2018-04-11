# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20180410_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 26, 22, 5, 12, 496708)),
        ),
        migrations.AlterField(
            model_name='culture',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
