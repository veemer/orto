# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_attachment_attachment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('price_words', models.CharField(max_length=128)),
                ('patient', models.ForeignKey(to='records.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
