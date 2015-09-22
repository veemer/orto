# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_auto_20150923_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='number',
            field=models.CharField(default="", max_length=128, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recordtemplate',
            name='recommendations',
            field=models.TextField(verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
    ]
