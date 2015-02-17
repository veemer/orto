# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='attachment_type',
            field=models.CharField(default='planogramm', max_length=64, verbose_name='\u0422\u0438\u043f', choices=[('planogramm', 'planogramm'), ('topogramm', 'topogramm'), ('R', 'R')]),
            preserve_default=False,
        ),
    ]
