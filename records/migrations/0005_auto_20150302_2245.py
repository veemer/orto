# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20150302_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='customer',
            field=models.CharField(max_length=128, verbose_name='\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a'),
            preserve_default=True,
        ),
    ]
