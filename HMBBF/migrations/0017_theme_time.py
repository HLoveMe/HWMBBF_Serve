# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0016_remove_theme_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='time',
            field=models.CharField(default='\u4e0d\u5fc5\u586b\u5199', max_length=256, verbose_name='\u5177\u4f53\u65f6\u95f4\u6bb5'),
        ),
    ]
