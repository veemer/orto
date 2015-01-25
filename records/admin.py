# -*- coding: utf-8 -*-

from django.contrib import admin
from records.models import Patient, Record

admin.site.register(Patient)
admin.site.register(Record)
