# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_auto_20150815_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='physioagreement',
            name='electrophoresis',
            field=models.BooleanField(default=False, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0444\u043e\u0440\u0435\u0437'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='physioagreement',
            name='magnetotherapy',
            field=models.BooleanField(default=False, verbose_name='\u041c\u0430\u0433\u043d\u0438\u0442\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='physioagreement',
            name='paraffin',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0430\u0440\u0430\u0444\u0438\u043d\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='physioagreement',
            name='document',
            field=models.CharField(max_length=128, verbose_name='\u041f\u0430\u0441\u0441\u043f\u043e\u0440\u0442 (\u0438\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='physioagreement',
            name='num_of_procedures_str',
            field=models.CharField(max_length=128, verbose_name='\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043d\u044f\u0442\u0438\u0439 (\u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2016, 2, 24), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
