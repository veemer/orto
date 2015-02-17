# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from records.views import PatientList, CreatePatient, UpdatePatient, RecordsList, CreateRecord, \
                          UpdateRecord, DetailRecord, CreateAttachments

from records.api import AttachmentsApiView, RecordsApiView

urlpatterns = patterns('',

    url(r'^$', login_required(PatientList.as_view()), name='patient_list'),

    url(r'^create_patient/$', CreatePatient.as_view(), name='create_patient'),
    url(r'^update_patient/(?P<pk>\d+)/$', UpdatePatient.as_view(), name='update_patient'),

    url(r'^records/(?P<pk>\d+)/$', RecordsList.as_view(), name='records_list'),
    url(r'^records/(?P<pk>\d+)/create/$', CreateRecord.as_view(), name='create_record'),
    url(r'^records/(?P<pk>\d+)/update/$', UpdateRecord.as_view(), name='update_record'),
    url(r'^records/(?P<pk>\d+)/detail/$', DetailRecord.as_view(), name='detail_record'),
    url(r'^records/(?P<pk>\d+)/attach/$', CreateAttachments.as_view(), name='create_attachments'),

    url(r'^print/$', TemplateView.as_view(template_name='records/print.html'), name='print'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'records/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^api/records/(?P<record_pk>\d+)/attachments$', AttachmentsApiView.as_view(), name='upload'),
    url(r'^api/records/(?P<record_pk>\d+)$', RecordsApiView.as_view(), name='records'),
    url(r'^api/records$', RecordsApiView.as_view(), name='records'),

)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))