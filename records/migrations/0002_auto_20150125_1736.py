# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import Group

class Migration(migrations.Migration):

    def create_groups(apps, schema_editor):
        Group.objects.create(name='doctors')
        Group.objects.create(name='managers')

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
