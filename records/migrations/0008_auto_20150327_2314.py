# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0007_auto_20150318_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='record',
            name='template',
            field=models.ForeignKey(related_name='template_record', verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d', blank=True, to='records.RecordTemplate', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2015, 9, 27), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
