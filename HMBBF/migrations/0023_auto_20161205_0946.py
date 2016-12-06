# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0022_auto_20161205_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='type',
        ),
        migrations.AlterField(
            model_name='theme',
            name='type_info',
            field=models.CharField(max_length=256, verbose_name='\u7c7b\u578b', choices=[(0, '\u5cf0\u4f1a\u6f14\u8bb2(\u7c7b\u578b\u7801:0)'), (1, '\u4e3b\u9898\u6f14\u8bb2(\u7c7b\u578b\u7801:1)')]),
        ),
    ]
