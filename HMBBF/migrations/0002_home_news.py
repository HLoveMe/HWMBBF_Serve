# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='\u6807\u9898')),
                ('title_en', models.TextField(verbose_name=b'title')),
            ],
        ),
    ]
