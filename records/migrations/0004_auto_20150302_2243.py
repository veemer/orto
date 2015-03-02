# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_agreement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreement',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='agreement',
            name='customer',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442\u0430', to='records.Patient'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='price',
            field=models.IntegerField(verbose_name='\u0421\u0443\u043c\u043c\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='price_words',
            field=models.CharField(max_length=128, verbose_name='\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e'),
            preserve_default=True,
        ),
    ]
