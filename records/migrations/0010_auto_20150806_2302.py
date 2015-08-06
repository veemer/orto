# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_auto_20150329_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysioAgreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('customer', models.CharField(max_length=128, verbose_name='\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a')),
                ('consumer', models.CharField(max_length=128, verbose_name='\u041f\u043e\u0442\u0440\u0435\u0431\u0438\u0442\u0435\u043b\u044c')),
                ('document', models.CharField(max_length=128, verbose_name='\u041f\u0430\u0441\u0441\u043f\u043e\u0440\u0442 (\u0438\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430)')),
                ('massage', models.BooleanField(default=False, verbose_name='\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438\u0439 \u043c\u0430\u0441\u0441\u0430\u0436')),
                ('physical', models.BooleanField(default=False, verbose_name='\u0417\u0430\u043d\u044f\u0442\u0438\u044f \u043b\u0435\u0447\u0435\u0431\u043d\u043e\u0439 \u0444\u0438\u0437\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043e\u0439')),
                ('num_of_courses', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0443\u0440\u0441\u043e\u0432')),
                ('num_of_procedures', models.IntegerField(verbose_name='\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043d\u044f\u0442\u0438\u0439\u0439')),
                ('procedure_price', models.IntegerField(verbose_name='C\u0443\u043c\u043c\u0430 \u0437\u0430 \u043a\u0430\u0436\u0434\u043e\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u0435')),
                ('price', models.IntegerField(verbose_name='\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c')),
                ('price_words', models.CharField(max_length=128, verbose_name='\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e')),
                ('patient', models.ForeignKey(verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442', to='records.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(default=datetime.date(2016, 2, 6), null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
