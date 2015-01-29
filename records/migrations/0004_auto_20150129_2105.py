# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0003_attachment_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(upload_to=b'', verbose_name='\u0424\u0430\u0439\u043b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='doctor',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='record',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u043f\u0438\u0441\u044c', to='records.Record'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(verbose_name='\u0410\u0434\u0440\u0435\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_day',
            field=models.DateField(verbose_name='\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='father_name',
            field=models.CharField(max_length=128, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='\u0418\u043c\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=64, verbose_name='\u041f\u043e\u043b', choices=[('m', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), ('w', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='organization',
            field=models.CharField(max_length=128, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='passport_issued_by',
            field=models.CharField(max_length=128, verbose_name='\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='passport_number',
            field=models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='passport_seria',
            field=models.IntegerField(verbose_name='\u0421\u0435\u0440\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_home',
            field=models.CharField(max_length=64, verbose_name='\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_mobile',
            field=models.CharField(max_length=64, verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=128, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='complaints',
            field=models.TextField(verbose_name='\u0416\u0430\u043b\u043e\u0431\u044b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='diagnosis',
            field=models.TextField(verbose_name='\u0414\u0438\u0430\u0433\u043d\u043e\u0437'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='doctor',
            field=models.ForeignKey(verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='local_status',
            field=models.TextField(verbose_name='\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='next_visit_date',
            field=models.DateField(verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='objective_status',
            field=models.TextField(verbose_name='\u041e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442', to='records.Patient'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='recommendations',
            field=models.TextField(verbose_name='\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='update_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='visit_date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
    ]
