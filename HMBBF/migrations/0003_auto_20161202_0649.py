# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0002_home_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_news',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='\u9996\u9875\u65b0\u95fb'),
        ),
        migrations.AlterField(
            model_name='home_news',
            name='title_en',
            field=models.CharField(max_length=1024, verbose_name='home_title'),
        ),
    ]
