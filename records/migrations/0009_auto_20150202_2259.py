# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20150129_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='allow_contacts',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='birth_cert_number',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='E-Mail', blank=True),
            preserve_default=True,
        ),
    ]
