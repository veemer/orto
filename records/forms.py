# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.models import modelformset_factory
from records.models import Attachment, Patient, RecordTemplate, Record, Agreement, PhysioAgreement


AttachmentFormset = modelformset_factory(Attachment, extra=5, exclude=['record', 'doctor'])


class PatientForm(ModelForm):

    class Meta:

        model = Patient
        exclude = ['created_by']


class RecordTemplateForm(ModelForm):

    class Meta:

        model = RecordTemplate
        exclude = ['doctor']


class RecordForm(ModelForm):

    class Meta:

        model = Record
        exclude = ['patient', 'doctor', 'visit_date', 'update_date']


class AgreementForm(ModelForm):

    class Meta:

        model = Agreement
        exclude = ['patient', 'date']


class PhysioAgreementForm(ModelForm):

    class Meta:

        model = PhysioAgreement
        exclude = ['patient', 'date']
