# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from records.views import PatientList, CreatePatient, UpdatePatient, RecordsList, \
                          CreateRecord, UpdateRecord, DetailRecord, CreateAttachments

urlpatterns = patterns('',

    url(r'^$', PatientList.as_view(), name='patient_list'),

    url(r'^create_patient/$', CreatePatient.as_view(), name='create_patient'),
    url(r'^update_patient/(?P<pk>\d+)/$', UpdatePatient.as_view(), name='update_patient'),

    url(r'^records_list/(?P<pk>\d+)/$', RecordsList.as_view(), name='records_list'),
    url(r'^records_list/(?P<pk>\d+)/create/$', CreateRecord.as_view(), name='create_record'),
    url(r'^records_list/(?P<pk>\d+)/update/$', UpdateRecord.as_view(), name='update_record'),
    url(r'^records_list/(?P<pk>\d+)/detail/$', DetailRecord.as_view(), name='detail_record'),
    url(r'^records_list/(?P<pk>\d+)/attach/$', CreateAttachments.as_view(), name='create_attachments'),

    url(r'^print/$', TemplateView.as_view(template_name='records/print.html'), name='print'),
)
