# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_auto_20150129_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='visit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
    ]
