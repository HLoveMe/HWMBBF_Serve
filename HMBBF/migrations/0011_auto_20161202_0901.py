# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0010_guest_home_ad_home_keyword_home_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='home_ad',
        ),
        migrations.DeleteModel(
            name='home_Keyword',
        ),
        migrations.DeleteModel(
            name='home_news',
        ),
    ]
