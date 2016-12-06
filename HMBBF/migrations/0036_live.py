# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0035_theme_theme_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='live',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('live_name', models.CharField(max_length=256, verbose_name='\u540d\u79f0')),
                ('time_begin', models.DateTimeField(verbose_name='beigin')),
                ('time_end', models.TimeField(verbose_name='end')),
                ('vedio_url', models.TextField(verbose_name='URL')),
                ('date', models.DateField(verbose_name='\u65e5\u671f')),
                ('time', models.TextField(verbose_name='\u65f6\u95f4\u6bb5', editable=False)),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u5f00\u59cb(\u72b6\u6001\u7801:0)'), (1, '\u8fdb\u884c\u4e2d(\u72b6\u6001\u7801:1)'), (2, '\u5df2\u7ed3\u675f(\u72b6\u6001\u7801:2)'), (3, '\u5373\u5c06\u5f00\u59cb(\u72b6\u6001\u7801:3)'), (4, '\u56de\u653e(\u72b6\u6001\u7801:4)')])),
                ('type', models.IntegerField(verbose_name='\u7c7b\u578b', choices=[(0, '\u5cf0\u4f1a\u6f14\u8bb2'), (1, '\u4e3b\u9898\u6f14\u8bb2')])),
                ('is_collect', models.BooleanField(verbose_name='\u662f\u5426\u6536\u85cf')),
                ('live_guest', models.ManyToManyField(to='HMBBF.Guest')),
            ],
        ),
    ]
