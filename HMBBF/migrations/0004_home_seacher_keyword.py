# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0003_auto_20161202_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_seacher_keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u70ed\u8bcd')),
                ('name_en', models.CharField(max_length=256, verbose_name='\u70ed\u8bcd')),
            ],
        ),
    ]
