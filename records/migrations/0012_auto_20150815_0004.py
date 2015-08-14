# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20150807_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='physioagreement',
            name='num_of_courses_str',
            field=models.CharField(default='', max_length=128, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0443\u0440\u0441\u043e\u0432 (\u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physioagreement',
            name='num_of_procedures_str',
            field=models.CharField(default='', max_length=128, verbose_name='\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043d\u044f\u0442\u0438\u0439\u0439 (\u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2016, 2, 15), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
