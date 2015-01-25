# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from records.views import PatientList, NewPatient, UpdatePatient

urlpatterns = patterns('',

    url(r'^$', PatientList.as_view(), name='patient_list'),
    url(r'^new_patient/$', NewPatient.as_view(), name='new_patient'),
    url(r'^update_patient/(?P<pk>\d+)/$', UpdatePatient.as_view(), name='update_patient')
)
