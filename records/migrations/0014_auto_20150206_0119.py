# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_auto_20150205_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='complaints',
            field=models.TextField(null=True, verbose_name='\u0416\u0430\u043b\u043e\u0431\u044b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='diagnosis',
            field=models.TextField(null=True, verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0437', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='local_status',
            field=models.TextField(null=True, verbose_name='\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='objective_status',
            field=models.TextField(null=True, verbose_name='\u041e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='recommendations',
            field=models.TextField(null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438', blank=True),
            preserve_default=True,
        ),
    ]
