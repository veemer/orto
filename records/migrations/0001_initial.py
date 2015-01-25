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
                ('description', models.TextField()),
                ('attachment', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('father_name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('birth_day', models.DateField()),
                ('gender', models.CharField(max_length=64, choices=[('m', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), ('w', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')])),
                ('phone_home', models.CharField(max_length=64)),
                ('phone_mobile', models.CharField(max_length=64)),
                ('organization', models.CharField(max_length=128)),
                ('passport_seria', models.IntegerField()),
                ('passport_number', models.IntegerField()),
                ('passport_issued_by', models.CharField(max_length=128)),
                ('address', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complaints', models.TextField()),
                ('objective_status', models.TextField()),
                ('local_status', models.TextField()),
                ('diagnosis', models.TextField()),
                ('recommendations', models.TextField()),
                ('visit_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('next_visit_date', models.DateField()),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(to='records.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attachment',
            name='record',
            field=models.ForeignKey(to='records.Record'),
            preserve_default=True,
        ),
    ]
