# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0020_auto_20161205_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='day',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='status_op',
        ),
        migrations.AlterField(
            model_name='theme',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u5f00\u59cb(\u72b6\u6001\u7801:0)'), (1, '\u8fdb\u884c\u4e2d(\u72b6\u6001\u7801:1)'), (2, '\u8fdb\u884c\u4e2d(\u72b6\u6001\u7801:2)'), (3, '\u8fdb\u884c\u4e2d(\u72b6\u6001\u7801:3)'), (4, '\u8fdb\u884c\u4e2d(\u72b6\u6001\u7801:4)')]),
        ),
    ]
