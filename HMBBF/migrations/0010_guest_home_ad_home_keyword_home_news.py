# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0009_auto_20161202_0900'),
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
        migrations.CreateModel(
            name='home_ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ad_name', models.CharField(max_length=1024, verbose_name='AD\u6807\u9898')),
                ('ad_name_en', models.CharField(max_length=1024, verbose_name='AD_EN_tiitle')),
                ('type', models.CharField(default=b'0', max_length=1024, verbose_name='\u7c7b\u578b')),
                ('target_id', models.CharField(max_length=1024, verbose_name='\u76ee\u6807ID')),
                ('banner_img', models.CharField(max_length=1024, verbose_name='\u56fe\u7247')),
                ('banner_img_en', models.CharField(max_length=1024, verbose_name='EN_\u56fe\u7247')),
                ('ad_url', models.CharField(max_length=1024, verbose_name='AD_URL')),
                ('ad_url_en', models.CharField(max_length=1024, verbose_name='AD_EN_URL')),
            ],
        ),
        migrations.CreateModel(
            name='home_Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u70ed\u8bcd')),
                ('name_en', models.CharField(max_length=256, verbose_name='keyword')),
            ],
        ),
        migrations.CreateModel(
            name='home_news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024, verbose_name='\u9996\u9875\u65b0\u95fb')),
                ('title_en', models.CharField(max_length=1024, verbose_name='home_title')),
            ],
        ),
    ]
