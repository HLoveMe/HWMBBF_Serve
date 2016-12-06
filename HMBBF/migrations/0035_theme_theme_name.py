# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0034_auto_20161205_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='theme_name',
            field=models.CharField(default=datetime.datetime(2016, 12, 5, 6, 59, 46, 414933, tzinfo=utc), max_length=256, verbose_name='\u540d\u79f0'),
            preserve_default=False,
        ),
    ]
