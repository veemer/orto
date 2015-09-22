# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_auto_20150824_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordtemplate',
            name='content',
        ),
        migrations.AddField(
            model_name='recordtemplate',
            name='diagnosis',
            field=models.TextField(default='', verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0437'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordtemplate',
            name='recommendations',
            field=models.TextField(default='', verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='physioagreement',
            name='num_of_courses_str',
            field=models.CharField(max_length=128, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0443\u0440\u0441\u043e\u0432 (\u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e)22'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2016, 3, 23), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
