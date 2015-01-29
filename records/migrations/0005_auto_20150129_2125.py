# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20150129_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='organization',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='passport_issued_by',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='passport_number',
            field=models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='passport_seria',
            field=models.IntegerField(null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_home',
            field=models.CharField(max_length=64, null=True, verbose_name='\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_mobile',
            field=models.CharField(max_length=64, null=True, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
            preserve_default=True,
        ),
    ]
