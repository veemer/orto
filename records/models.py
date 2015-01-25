# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

GENDER = (
        (u'm', u'Мужской'),
        (u'w', u'Женский')
)


class Patient(models.Model):

    first_name = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    birth_day = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=64)

    phone_home = models.CharField(max_length=64)
    phone_mobile = models.CharField(max_length=64)

    organization = models.CharField(max_length=128)

    passport_seria = models.IntegerField()
    passport_number = models.IntegerField()
    passport_issued_by = models.CharField(max_length=128)

    address = models.TextField()

    def __unicode__(self):
        return u'{} {} {}'.format(self.first_name, self.father_name, self.surname)


class Record(models.Model):

    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(User)

    complaints = models.TextField()
    objective_status = models.TextField()
    local_status = models.TextField()

    diagnosis = models.TextField()
    recommendations = models.TextField()

    visit_date = models.DateTimeField()
    update_date = models.DateTimeField()
    next_visit_date = models.DateField()


class Attachment(models.Model):

    record = models.ForeignKey(Record)
    description = models.TextField()
    attachment = models.FileField()
