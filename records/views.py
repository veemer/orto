# -*- coding: utf-8 -*-

import csv
import json
from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView

from django.core.urlresolvers import reverse_lazy

from dateutil.relativedelta import relativedelta

from records.models import Patient, Record, Agreement, RecordTemplate, PhysioAgreement
from records.forms import AttachmentFormset, PatientForm, RecordForm, AgreementForm, \
                          PhysioAgreementForm, RecordTemplateForm


# Patients

class PatientList(ListView):

    model = Patient
    paginate_by = 10
    template = 'records/patient_list.html'
    context_object_name = 'patient_list'

    def get_queryset(self):

        qs = super(PatientList, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(surname__icontains=q)

        return qs

    def get_context_data(self, **kwargs):

        context = super(PatientList, self).get_context_data(**kwargs)

        q = self.request.GET.get('q')
        if q:
            context['q'] = q

        today = timezone.localtime(timezone.now())
        context['born_today_cnt'] = Patient.objects.filter(birth_day__day=today.day,
                                                           birth_day__month=today.month).count()

        context['visit_this_week_cnt'] = Patient.this_week_objects.count()

        return context


class PatientBornTodayList(ListView):

    model = Patient
    template_name = 'records/patient_born_today_list.html'
    context_object_name = 'patient_list'

    def get_queryset(self):

        qs = super(PatientBornTodayList, self).get_queryset()
        today = timezone.localtime(timezone.now())

        return qs.filter(birth_day__day=today.day, birth_day__month=today.month)


class PatientVisitThisWeek(ListView):

    model = Patient
    template_name = 'records/patient_visit_this_week_list.html'
    context_object_name = 'patient_list'

    def get_queryset(self):

        return Patient.this_week_objects.all()


class PatientCsvList(ListView):

    model = Patient
    context_object_name = 'patient_list'
    csv_prefix = 'patient-list'

    def get_queryset(self):

        qs = super(PatientCsvList, self).get_queryset()
        return qs.filter(allow_contacts=True)

    def render_to_response(self, context, **response_kwargs):

        now_str = timezone.localtime(timezone.now()).strftime('%Y-%m-%d_%H:%M')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}-{}.csv"'.format(self.csv_prefix, now_str)

        writer = csv.writer(response)

        row = [u'Фамилия', u'Имя', u'Отчество', u'Мобильный телефон', u'E-mail']
        row = [s.encode('utf-8') for s in row]
        writer.writerow(row)

        for patient in context[self.context_object_name]:
            row = [patient.surname, patient.first_name, patient.father_name, patient.phone_mobile, patient.email]
            row = [s.encode('utf-8') for s in row]
            writer.writerow(row)

        return response


class PatientBornTodayCsvList(PatientCsvList):

    csv_prefix = 'patient-born-today'

    def get_queryset(self):

        qs = super(PatientBornTodayCsvList, self).get_queryset()
        today = timezone.localtime(timezone.now())

        return qs.filter(birth_day__day=today.day, birth_day__month=today.month)


class PatientVisitThisWeekCsvList(PatientCsvList):

    csv_prefix = 'patient-visit-this-week'

    def get_queryset(self):
        return Patient.this_week_objects.all()


class CreatePatient(CreateView):
    form_class = PatientForm
    template_name = 'records/create_patient.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreatePatient, self).form_valid(form)


class UpdatePatient(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'records/create_patient.html'
    success_url = reverse_lazy('patient_list')


# Records

class RecordsList(ListView):

    model = Record
    paginate_by = 10
    template_name = 'records/records_list.html'
    context_object_name = 'records_list'

    def dispatch(self, request, *args, **kwargs):
        self.patient_id = kwargs.get('pk')
        self.patient = get_object_or_404(Patient, id=self.patient_id)

        return super(RecordsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(RecordsList, self).get_queryset()
        return qs.filter(patient=self.patient)

    def get_context_data(self, **kwargs):
        context = super(RecordsList, self).get_context_data(**kwargs)
        context['patient'] = self.patient

        return context


class RecordTemplatesMixin(object):

    def get_context_data(self, **kwargs):

        context = super(RecordTemplatesMixin, self).get_context_data(**kwargs)
        templates = RecordTemplate.objects.filter(doctor=self.request.user)
        templates_list = [{'value': template.id,
                           'label': template.name,
                           'diagnosis': template.diagnosis,
                           'recommendations': template.recommendations} for template in templates]

        context['templates'] = json.dumps(templates_list)

        return context


class CreateRecord(RecordTemplatesMixin, CreateView):

    form_class = RecordForm
    template_name = 'records/create_record.html'

    def dispatch(self, request, *args, **kwargs):
        self.patient = get_object_or_404(Patient, pk=kwargs.get('pk'))
        return super(CreateRecord, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('records_list', args=(self.patient.pk,))

    def get_context_data(self, **kwargs):
        context = super(CreateRecord, self).get_context_data(**kwargs)
        context['patient'] = self.patient

        next_visit_date = timezone.localtime(timezone.now()).date() + relativedelta(months=6)
        context['next_visit_date'] = next_visit_date.strftime("%d.%m.%Y")
        context['template_id'] = -1

        return context

    def form_valid(self, form):

        form.instance.doctor = self.request.user
        form.instance.patient = self.patient

        return super(CreateRecord, self).form_valid(form)


class UpdateRecord(RecordTemplatesMixin, UpdateView):

    model = Record
    form_class = RecordForm
    template_name = 'records/create_record.html'

    def dispatch(self, request, *args, **kwargs):
        self.record = get_object_or_404(Record, pk=kwargs.get('pk'))
        return super(UpdateRecord, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('records_list', args=(self.record.patient_id,))

    def get_context_data(self, **kwargs):

        context = super(UpdateRecord, self).get_context_data(**kwargs)

        if self.record.template is None:
            context['template_id'] = -1
        else:
            context['template_id'] = self.record.template.id

        context['record'] = self.record
        context['patient'] = self.record.patient

        return context


class DetailRecord(DetailView):
    model = Record
    context_object_name = 'record'
    template_name = 'records/detail_record.html'

    def get_context_data(self, **kwargs):

        context = super(DetailRecord, self).get_context_data()
        context['can_print'] = True
        if self.request.GET.get('print', None) is not None:
            context['print'] = True

        return context


class CreateAttachments(FormView):
    template_name = 'records/create_attachments.html'
    form_class = AttachmentFormset


# Agreements

class AgreementsList(ListView):

    model = Agreement
    paginate_by = 10
    context_object_name = 'agreements_list'
    template_name = 'records/agreements_list.html'

    def dispatch(self, request, *args, **kwargs):

        self.patient_id = kwargs.get('pk')
        self.patient = get_object_or_404(Patient, id=self.patient_id)

        return super(AgreementsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        qs = super(AgreementsList, self).get_queryset()
        return qs.filter(patient=self.patient)

    def get_context_data(self, **kwargs):

        context = super(AgreementsList, self).get_context_data(**kwargs)
        context['patient'] = self.patient

        return context


class PhysioAgreementsList(AgreementsList):

    model = PhysioAgreement
    template_name = 'records/physio_agreements_list.html'


class AgreementCreate(CreateView):

    model = Agreement
    form_class = AgreementForm
    template_name = 'records/agreement_create.html'

    def dispatch(self, request, *args, **kwargs):

        self.patient_id = kwargs.get('pk')
        self.patient = get_object_or_404(Patient, id=self.patient_id)

        return super(AgreementCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        form.instance.patient = self.patient
        return super(AgreementCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('agreements_list', args=(self.patient.pk,))

    def get_context_data(self, **kwargs):

        context = super(AgreementCreate, self).get_context_data(**kwargs)
        context['patient'] = self.patient

        return context


class PhysioAgreementCreate(AgreementCreate):

    model = PhysioAgreement
    form_class = PhysioAgreementForm
    template_name = 'records/physio_agreement_create.html'

    def get_success_url(self):
        return reverse_lazy('physio_agreements_list', args=(self.patient.pk,))


class AgreementDetail(DetailView):

    model = Agreement
    context_object_name = 'agreement'
    template_name = 'records/agreement_detail.html'

    def get_context_data(self, **kwargs):

        context = super(AgreementDetail, self).get_context_data(**kwargs)
        context['can_print'] = True
        if self.request.GET.get('print', None) is not None:
            context['print'] = True

        return context


class PhysioAgreementDetail(AgreementDetail):

    model = PhysioAgreement
    template_name = 'records/physio_agreement_detail.html'


# Records Templates

class TemplateList(ListView):

    model = RecordTemplate
    context_object_name = 'templates'
    template_name = 'records/template_list.html'

    def get_queryset(self):

        qs = super(TemplateList, self).get_queryset()
        return qs.filter(doctor=self.request.user)


class CreateTemplate(CreateView):

    model = RecordTemplate
    form_class = RecordTemplateForm
    template_name = 'records/template_create.html'

    def get_success_url(self):
        return reverse_lazy('template_list')

    def form_valid(self, form):

        form.instance.doctor = self.request.user
        return super(CreateTemplate, self).form_valid(form)


class UpdateTemplate(UpdateView):

    model = RecordTemplate
    form_class = RecordTemplateForm
    template_name = 'records/template_create.html'

    def get_success_url(self):
        return reverse_lazy('template_list')
