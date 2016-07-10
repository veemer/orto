# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0017_auto_20150928_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='address',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='agreement',
            name='phone',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2017, 1, 11), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
