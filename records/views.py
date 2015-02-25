# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView

from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.formsets import formset_factory

from records.models import Patient, Record, Attachment, Agreement
from records.forms import AttachmentFormset, PatientForm, RecordForm, AgreementForm


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

        return context


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


class CreateRecord(CreateView):

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

        return context

    def form_valid(self, form):

        form.instance.doctor = self.request.user
        form.instance.patient = self.patient

        return super(CreateRecord, self).form_valid(form)


class UpdateRecord(UpdateView):

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
    context_object_name = 'agreements'
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


class AgreementDetail(DetailView):

    model = Agreement
    context_object_name = 'agreement'
    template_name = 'records/agreement_detail.html'
