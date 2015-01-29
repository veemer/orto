# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView

from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.formsets import formset_factory

from records.models import Patient, Record, Attachment
from records.forms import AttachmentFormset

class PatientList(ListView):

    model = Patient
    paginate_by = 100
    template = 'records/patient_list.html'
    context_object_name = 'patient_list'


class CreatePatient(CreateView):
    model = Patient
    template_name = 'records/create_patient.html'
    success_url = reverse_lazy('patient_list')


class UpdatePatient(UpdateView):
    model = Patient
    template_name = 'records/create_patient.html'
    success_url = reverse_lazy('patient_list')


class RecordsList(ListView):

    model = Record
    paginate_by = 100
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

    model = Record
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


class UpdateRecord(UpdateView):

    model = Record
    template_name = 'records/create_record.html'

    def dispatch(self, request, *args, **kwargs):
        self.record = get_object_or_404(Record, pk=kwargs.get('pk'))
        return super(UpdateRecord, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('records_list', args=(self.record.patient_pk,))

    def get_context_data(self, **kwargs):
        context = super(UpdateRecord, self).get_context_data(**kwargs)
        context['patient'] = self.record.patient

        return context


class DetailRecord(DetailView):
    model = Record
    context_object_name = 'record'
    template_name = 'records/detail_record.html'


class CreateAttachments(FormView):
    template_name = 'records/create_attachments.html'
    form_class = AttachmentFormset