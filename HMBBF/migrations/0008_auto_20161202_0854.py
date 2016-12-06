# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0007_auto_20161202_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='guest_id',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='guest_type',
        ),
        migrations.AddField(
            model_name='guest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=datetime.datetime(2016, 12, 2, 8, 54, 34, 235706, tzinfo=utc), serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='is_collect',
            field=models.BigIntegerField(default=False, choices=[(0, True), (1, False)]),
        ),
    ]
