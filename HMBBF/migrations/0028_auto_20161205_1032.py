# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0027_auto_20161205_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='video',
            new_name='vedio_url',
        ),
    ]
