# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20150806_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='physioagreement',
            name='responsible',
            field=models.CharField(default='', max_length=128, verbose_name='\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='physioagreement',
            name='price_words',
            field=models.CharField(max_length=128, verbose_name='\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2016, 2, 7), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
