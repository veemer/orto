# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20150205_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.ImageField(upload_to=b'attachments/%Y/%m/%d', verbose_name='\u0424\u0430\u0439\u043b'),
            preserve_default=True,
        ),
    ]
