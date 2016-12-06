# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0013_home_ad_home_keyword_home_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_begin', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('vedio_url', models.CharField(max_length=256, verbose_name='\u89c6\u9891\u5730\u5740')),
                ('video_type', models.CharField(max_length=256, verbose_name='\u7c7b\u578b')),
                ('time_end', models.DateTimeField(verbose_name='\u4ecb\u7ecd\u65f6\u95f4')),
                ('address', models.CharField(max_length=256, verbose_name='\u5730\u70b9')),
                ('day', models.IntegerField(verbose_name='\u7b2c\u51e0\u5929')),
                ('type', models.IntegerField(verbose_name='\u7c7b\u578b\u7801')),
                ('type_info', models.CharField(max_length=256, verbose_name='\u7c7b\u578b')),
                ('is_collect', models.BooleanField(verbose_name='\u662f\u5426\u6536\u85cf', choices=[(0, True), (1, False)])),
                ('date', models.DateField(verbose_name='\u65f6\u95f4')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001\u7801', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])),
                ('status_op', models.CharField(max_length=256, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u5f00\u59cb'), (1, '\u8fdb\u884c\u4e2d'), (2, '\u5df2\u7ed3\u675f'), (3, '\u5373\u5c06\u5f00\u59cb'), (4, '\u56de\u653e')])),
                ('theme_guest', models.ForeignKey(to='HMBBF.Guest')),
            ],
        ),
    ]
