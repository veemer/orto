# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy

from records.models import Patient


class PatientList(ListView):

    model = Patient
    paginate_by = 100
    template = 'records/patient_list.html'
    context_object_name = 'patient_list'


class NewPatient(CreateView):
    model = Patient
    template_name = 'records/new_patient.html'
    success_url = reverse_lazy('patient_list')


class UpdatePatient(UpdateView):
    model = Patient
    template_name = 'records/new_patient.html'
    success_url = reverse_lazy('patient_list')
