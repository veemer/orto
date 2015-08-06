# -*- coding: utf-8 -*-

from django.contrib import admin
from records.models import Patient, Record, Attachment, Agreement, PhysioAgreement

admin.site.register(Patient)
admin.site.register(Record)
admin.site.register(Attachment)
admin.site.register(Agreement)
admin.site.register(PhysioAgreement)
