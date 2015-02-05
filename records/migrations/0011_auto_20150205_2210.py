# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20150202_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.ImageField(upload_to=b'', verbose_name='\u0424\u0430\u0439\u043b'),
            preserve_default=True,
        ),
    ]
