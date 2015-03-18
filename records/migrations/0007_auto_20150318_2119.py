# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User, Group


def create_groups(apps, schema_editor):

    doctors_group = Group.objects.create(name='doctors')
    technics_group = Group.objects.create(name='technics')
    managers_group = Group.objects.create(name='managers')

    doctors = [User.objects.create(username='lukash', first_name=u'Лукаш Ю.В.', password='mb8zf'),
               User.objects.create(username='volkova', first_name=u'Волкова Е.Н.', password='79cgt'),
               User.objects.create(username='kislovskaya', first_name=u'Кисловская Е.Ю', password='zktj0'),
               User.objects.create(username='ryabokonev', first_name=u'Рябоконев С.Г.', password='mgwpb'),
               User.objects.create(username='vasilcova', first_name=u'Васильцова Д.В.', password='nxb1l')]

    technic = User.objects.create(username='technic', password='gpzzk')
    manager = User.objects.create(username='manager', password='1k2uw')

    doctors_group.user_set.add(*doctors)
    technics_group.user_set.add(technic)
    managers_group.user_set.add(manager)


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20150304_0828'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
