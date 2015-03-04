# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20150302_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='consumer',
            field=models.CharField(default='', max_length=128, verbose_name='\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agreement',
            name='document',
            field=models.CharField(default='', max_length=128, verbose_name='\u041f\u0430\u0441\u0441\u043f\u043e\u0440\u0442 (\u0438\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430)'),
            preserve_default=False,
        ),
    ]
