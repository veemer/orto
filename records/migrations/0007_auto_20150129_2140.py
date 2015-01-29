# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20150129_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f', auto_now_add=True),
            preserve_default=True,
        ),
    ]
