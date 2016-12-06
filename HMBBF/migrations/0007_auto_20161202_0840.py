# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMBBF', '0006_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='guest_id',
            field=models.AutoField(verbose_name='ID', serialize=False, editable=False, primary_key=True),
        ),
    ]
