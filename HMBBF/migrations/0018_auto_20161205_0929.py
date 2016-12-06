# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0017_theme_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='theme_guest',
        ),
        migrations.AddField(
            model_name='theme',
            name='theme_guest',
            field=models.ManyToManyField(to='HMBBF.Guest'),
        ),
    ]
