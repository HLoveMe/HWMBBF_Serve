# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0005_auto_20161202_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guest_id', models.IntegerField(serialize=False, verbose_name='ID', primary_key=True)),
                ('guest_type', models.IntegerField(verbose_name='\u7c7b\u578b')),
                ('avatar', models.URLField(verbose_name='\u5934\u50cf')),
                ('guest_name', models.CharField(max_length=256, verbose_name='\u540d\u79f0')),
                ('company', models.CharField(max_length=256, verbose_name='\u516c\u53f8')),
                ('position', models.CharField(max_length=256, verbose_name='\u804c\u4f4d')),
            ],
        ),
    ]
