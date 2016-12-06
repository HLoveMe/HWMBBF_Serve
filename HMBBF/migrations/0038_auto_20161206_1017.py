# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0037_auto_20161206_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='live_guest',
            field=models.ManyToManyField(to='HMBBF.Guest', blank=True),
        ),
    ]
