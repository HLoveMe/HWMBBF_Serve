# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0033_auto_20161205_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='type_info',
            new_name='type',
        ),
    ]
