# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0025_remove_theme_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='video_type',
            new_name='vedio_type',
        ),
    ]
