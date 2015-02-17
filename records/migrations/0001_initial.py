# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('attachment', models.ImageField(upload_to=b'attachments/%Y/%m/%d', verbose_name='\u0424\u0430\u0439\u043b')),
                ('doctor', models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f')),
                ('father_name', models.CharField(max_length=128, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('surname', models.CharField(max_length=128, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('birth_day', models.DateField(verbose_name='\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('gender', models.CharField(max_length=64, verbose_name='\u041f\u043e\u043b', choices=[('m', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), ('w', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')])),
                ('phone_home', models.CharField(max_length=64, null=True, verbose_name='\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('phone_mobile', models.CharField(max_length=64, null=True, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='E-Mail', blank=True)),
                ('allow_contacts', models.BooleanField(default=False, verbose_name='C\u043e\u0433\u043b\u0430\u0441\u0435\u043d \u043d\u0430 CMC, E-Mail \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0443 \u0438 \u043e\u043f\u0440\u043e\u0441 \u043e \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433')),
                ('organization', models.CharField(max_length=128, null=True, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', blank=True)),
                ('passport_seria', models.IntegerField(null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f', blank=True)),
                ('passport_number', models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440', blank=True)),
                ('passport_issued_by', models.CharField(max_length=128, null=True, verbose_name='\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d', blank=True)),
                ('birth_cert_number', models.CharField(max_length=128, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430 \u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0438', blank=True)),
                ('address', models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('status', models.CharField(default=b'green', max_length=128, choices=[('red', 'red'), ('green', 'green'), ('yellow', 'yellow')])),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complaints', models.TextField(null=True, verbose_name='\u0416\u0430\u043b\u043e\u0431\u044b', blank=True)),
                ('objective_status', models.TextField(null=True, verbose_name='\u041e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441', blank=True)),
                ('local_status', models.TextField(null=True, verbose_name='\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441', blank=True)),
                ('diagnosis', models.TextField(null=True, verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0437', blank=True)),
                ('recommendations', models.TextField(null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438', blank=True)),
                ('visit_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f', auto_now_add=True)),
                ('next_visit_date', models.DateField(null=True, verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f', blank=True)),
                ('doctor', models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442', to='records.Patient')),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attachment',
            name='record',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u043f\u0438\u0441\u044c', to='records.Record'),
            preserve_default=True,
        ),
    ]
