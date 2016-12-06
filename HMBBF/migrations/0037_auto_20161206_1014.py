# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0036_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='time_begin',
            field=models.TimeField(verbose_name='beigin'),
        ),
    ]
