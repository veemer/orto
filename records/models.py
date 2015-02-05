# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

GENDER = (
        (u'm', u'Мужской'),
        (u'w', u'Женский')
)

PATIENT_STATUS = (
    (u'red', u'red'),
    (u'green', u'green'),
    (u'yellow', u'yellow')
)

class Patient(models.Model):

    first_name = models.CharField(max_length=128, verbose_name=u'Имя')
    father_name = models.CharField(max_length=128, verbose_name=u'Отчество')
    surname = models.CharField(max_length=128, verbose_name=u'Фамилия')

    birth_day = models.DateField(verbose_name=u'День рождения')
    gender = models.CharField(choices=GENDER, max_length=64, verbose_name=u'Пол')

    phone_home = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Домашний телефон')
    phone_mobile = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'Мобильный телефон')
    email = models.EmailField(blank=True, null=True, verbose_name=u'E-Mail')

    allow_contacts = models.BooleanField(default=False, verbose_name=u'Cогласен на CMC, E-Mail рассылку и опрос о качестве проведенных услуг')

    organization = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Организация')

    passport_seria = models.IntegerField(blank=True, null=True, verbose_name=u'Серия')
    passport_number = models.IntegerField(blank=True, null=True, verbose_name=u'Номер')
    passport_issued_by = models.CharField(blank=True, null=True, max_length=128, verbose_name=u'Кем выдан')

    birth_cert_number = models.CharField(blank=True, null=True, max_length=128, verbose_name=u'Номер свидетельства о рождении')

    address = models.TextField(blank=True, null=True, verbose_name=u'Адрес')

    status = models.CharField(max_length=128, choices=PATIENT_STATUS, default='green')

    created_by = models.ForeignKey(User)

    def __unicode__(self):

        return u'{} {} {}'.format(self.first_name, self.father_name, self.surname)


class Record(models.Model):

    patient = models.ForeignKey(Patient, verbose_name=u'Пациент')
    doctor = models.ForeignKey(User, verbose_name=u'Доктор')

    complaints = models.TextField(verbose_name=u'Жалобы')
    objective_status = models.TextField(verbose_name=u'Объективный статус')
    local_status = models.TextField(verbose_name=u'Локальный статус')

    diagnosis = models.TextField(verbose_name=u'Диагноз')
    recommendations = models.TextField(verbose_name=u'Рекомендации')

    visit_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата посещения')
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name=u'Дата изменения')
    next_visit_date = models.DateField(verbose_name=u'Рекомендуемая дата посещения')

    def __unicode__(self):

        return u'{} - {}'.format(self.patient, self.visit_date)


class Attachment(models.Model):

    doctor = models.ForeignKey(User, verbose_name=u'Доктор')
    record = models.ForeignKey(Record, verbose_name=u'Запись')
    description = models.TextField(verbose_name=u'Описание', blank=True, null=True)
    attachment = models.ImageField(verbose_name=u'Файл', upload_to='attachments/%Y/%m/%d')

    def __unicode__(self):

        return u'{} - {}'.format(self.record, self.attachment.name)