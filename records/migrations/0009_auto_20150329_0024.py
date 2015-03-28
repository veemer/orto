# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20150327_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2015, 9, 29), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='template',
            field=models.OneToOneField(related_name='template_record', null=True, blank=True, to='records.RecordTemplate', verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recordtemplate',
            name='content',
            field=models.TextField(verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recordtemplate',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
