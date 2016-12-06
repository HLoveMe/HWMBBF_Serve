# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0023_auto_20161205_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='time_begin',
            field=models.TimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='time_end',
            field=models.TimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
    ]
