# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 10:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myaims', '0004_auto_20160608_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aim',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 10, 3, 35, 556491, tzinfo=utc)),
        ),
    ]