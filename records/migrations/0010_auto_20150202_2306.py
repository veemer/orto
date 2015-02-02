# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_auto_20150202_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(default=b'green', max_length=128, choices=[('red', 'red'), ('green', 'green'), ('yellow', 'yellow')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='allow_contacts',
            field=models.BooleanField(default=False, verbose_name='C\u043e\u0433\u043b\u0430\u0441\u0435\u043d \u043d\u0430 CMC, E-Mail \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0443 \u0438 \u043e\u043f\u0440\u043e\u0441 \u043e \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433'),
            preserve_default=True,
        ),
    ]
