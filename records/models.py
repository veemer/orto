# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

GENDER = (
        (u'm', u'Мужской'),
        (u'w', u'Женский')
)


class Patient(models.Model):

    first_name = models.CharField(max_length=128, verbose_name=u'Имя')
    father_name = models.CharField(max_length=128, verbose_name=u'Отчество')
    surname = models.CharField(max_length=128, verbose_name=u'Фамилия')

    birth_day = models.DateField(verbose_name=u'День рождения')
    gender = models.CharField(choices=GENDER, max_length=64, verbose_name=u'Пол')

    phone_home = models.CharField(max_length=64, verbose_name=u'Домашний телефон')
    phone_mobile = models.CharField(max_length=64, verbose_name=u'Мобильный телефон')

    organization = models.CharField(max_length=128, verbose_name=u'Организация')

    passport_seria = models.IntegerField(verbose_name=u'Серия')
    passport_number = models.IntegerField(verbose_name=u'Номер')
    passport_issued_by = models.CharField(max_length=128, verbose_name=u'Кем выдан')

    address = models.TextField(verbose_name=u'Адрес')

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

    visit_date = models.DateTimeField(verbose_name=u'Дата посещения')
    update_date = models.DateTimeField(verbose_name=u'Дата изменения')
    next_visit_date = models.DateField(verbose_name=u'Рекомендуемая дата посещения')


class Attachment(models.Model):

    doctor = models.ForeignKey(User, verbose_name=u'Доктор')
    record = models.ForeignKey(Record, verbose_name=u'Запись')
    description = models.TextField(verbose_name=u'Описание')
    attachment = models.FileField(verbose_name=u'Файл')
