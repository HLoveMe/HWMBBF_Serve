# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0026_auto_20161205_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='vedio_url',
            new_name='video',
        ),
    ]
