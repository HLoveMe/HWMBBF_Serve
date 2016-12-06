# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0019_auto_20161205_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='is_collect',
            field=models.BooleanField(default=1, verbose_name='\u662f\u5426\u6536\u85cf', choices=[(0, True), (1, False)]),
        ),
    ]
