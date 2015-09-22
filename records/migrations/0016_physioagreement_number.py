# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0015_auto_20150923_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='physioagreement',
            name='number',
            field=models.CharField(default='', max_length=128, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430'),
            preserve_default=False,
        ),
    ]
