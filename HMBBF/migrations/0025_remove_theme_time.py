# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0024_auto_20161205_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='time',
        ),
    ]
