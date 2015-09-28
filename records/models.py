# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from records.managers import ThisWeekManager


GENDER = (
    (u'm', u'Мужской'),
    (u'w', u'Женский')
)

PATIENT_STATUS = (
    (u'red', u'red'),
    (u'green', u'green'),
    (u'yellow', u'yellow')
)

ATTACHMENT_TYPE = (
    (u'planogramm', u'planogramm'),
    (u'topogramm', u'topogramm'),
    (u'R', u'R')
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

    allow_contacts = models.BooleanField(
        default=False, verbose_name=u'Cогласен на CMC, E-Mail рассылку и опрос о качестве проведенных услуг')

    organization = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'Организация')

    passport_seria = models.IntegerField(blank=True, null=True, verbose_name=u'Серия')
    passport_number = models.IntegerField(blank=True, null=True, verbose_name=u'Номер')
    passport_issued_by = models.CharField(blank=True, null=True, max_length=128, verbose_name=u'Кем выдан')

    birth_cert_number = models.CharField(
        blank=True, null=True, max_length=128, verbose_name=u'Номер свидетельства о рождении')

    address = models.TextField(blank=True, null=True, verbose_name=u'Адрес')

    status = models.CharField(max_length=128, choices=PATIENT_STATUS, default='green')

    created_by = models.ForeignKey(User)

    objects = models.Manager()
    this_week_objects = ThisWeekManager()

    def has_passport(self):
        return self.passport_seria and self.passport_number and self.passport_issued_by

    def get_age(self):

        today = timezone.localtime(timezone.now())
        return today.year - self.birth_day.year

    def get_next_visit_date(self):

        record = Record.objects.filter(patient=self).order_by('-next_visit_date').first()
        if record:
            return record.next_visit_date

    def __unicode__(self):

        return u'{} {} {}'.format(self.first_name, self.father_name, self.surname)


class RecordTemplate(models.Model):

    doctor = models.ForeignKey(User)
    name = models.CharField(max_length=128, verbose_name=u'Название')
    diagnosis = models.TextField(verbose_name=u'Диагноз')
    recommendations = models.TextField(verbose_name=u'Рекомендации')

    def __unicode__(self):

        return self.name


class Record(models.Model):

    patient = models.ForeignKey(Patient, verbose_name=u'Пациент')
    doctor = models.ForeignKey(User, verbose_name=u'Доктор')

    complaints = models.TextField(verbose_name=u'Жалобы', blank=True, null=True)
    objective_status = models.TextField(verbose_name=u'Объективный статус', blank=True, null=True)
    local_status = models.TextField(verbose_name=u'Локальный статус', blank=True, null=True)

    diagnosis = models.TextField(verbose_name=u'Диагноз', blank=True, null=True)
    recommendations = models.TextField(verbose_name=u'Рекомендации', blank=True, null=True)

    visit_date = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата посещения')
    update_date = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name=u'Дата изменения')
    next_visit_date = models.DateField(verbose_name=u'Рекомендуемая дата посещения', blank=True, null=True,
                                       default=timezone.localtime(timezone.now()).date() + relativedelta(months=6))

    template = models.ForeignKey(RecordTemplate, blank=True, null=True, verbose_name=u'Шаблон',
                                 related_name='template_record')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):

        return u'{} - {}'.format(self.patient, self.visit_date)


class Attachment(models.Model):

    doctor = models.ForeignKey(User, verbose_name=u'Доктор')
    record = models.ForeignKey(Record, verbose_name=u'Запись')
    description = models.TextField(verbose_name=u'Описание', blank=True, null=True)
    attachment = models.ImageField(verbose_name=u'Файл', upload_to='attachments/%Y/%m/%d')
    attachment_type = models.CharField(max_length=64, choices=ATTACHMENT_TYPE, verbose_name=u'Тип')

    def __unicode__(self):

        return u'{} - {}'.format(self.record, self.attachment.name)


class Agreement(models.Model):

    number = models.CharField(max_length=128, verbose_name=u'Номер документа')
    patient = models.ForeignKey(Patient, verbose_name=u'Пациента')
    date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    price = models.IntegerField(verbose_name=u'Сумма')
    price_words = models.CharField(max_length=128, verbose_name=u'Сумма прописью')

    customer = models.CharField(max_length=128, verbose_name=u'Заказчик')
    consumer = models.CharField(max_length=128, verbose_name=u'Потребитель')
    document = models.CharField(max_length=128, verbose_name=u'Пасспорт (иной документа)')

    class Meta:
        ordering = ['-id']

    def get_number(self):
        return self.number

    def __unicode__(self):
        return u'{}:{}'.format(self.patient, self.get_number())


class PhysioAgreement(models.Model):

    number = models.CharField(max_length=128, verbose_name=u'Номер договора')

    date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')

    patient = models.ForeignKey(Patient, verbose_name=u'Пациент')

    customer = models.CharField(max_length=128, verbose_name=u'Заказчик')
    consumer = models.CharField(max_length=128, verbose_name=u'Потребитель')
    document = models.CharField(max_length=128, verbose_name=u'Пасспорт (иной документ)')

    massage = models.BooleanField(default=False, verbose_name=u'Медицинский массаж')
    physical = models.BooleanField(default=False, verbose_name=u'Занятия лечебной физкультурой')
    paraffin = models.BooleanField(default=False, verbose_name=u'Парафинотерапия')
    electrophoresis = models.BooleanField(default=False, verbose_name=u'Электрофорез')
    magnetotherapy = models.BooleanField(default=False, verbose_name=u'Магнитотерапия')

    num_of_courses = models.IntegerField(verbose_name=u'Количество курсов')
    num_of_courses_str = models.CharField(max_length=128, verbose_name=u'Количество курсов (прописью)22')

    num_of_procedures = models.IntegerField(verbose_name=u'Общее количество занятийй')
    num_of_procedures_str = models.CharField(max_length=128, verbose_name=u'Общее количество занятий (прописью)')

    procedure_price = models.IntegerField(verbose_name=u'Cумма за каждое занятие')
    price = models.IntegerField(verbose_name=u'Общая стоимость')
    price_words = models.CharField(max_length=128, verbose_name=u'Общая стоимость прописью')

    responsible = models.CharField(max_length=128, verbose_name=u'Ответственный Исполнитель')

    def get_number(self):
        return self.number

    def __unicode__(self):
        return u'{}:{}'.format(self.patient, self.get_number())
