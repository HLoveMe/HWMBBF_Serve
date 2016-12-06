# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0011_auto_20161202_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.URLField(verbose_name='\u5934\u50cf')),
                ('guest_name', models.CharField(max_length=256, verbose_name='\u540d\u79f0')),
                ('company', models.CharField(max_length=256, verbose_name='\u516c\u53f8')),
                ('position', models.CharField(max_length=256, verbose_name='\u804c\u4f4d')),
                ('is_collect', models.BigIntegerField(default=False, choices=[(0, True), (1, False)])),
            ],
        ),
    ]
