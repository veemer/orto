# -*- coding: utf-8 -*-

from rest_framework import serializers
from records.models import Attachment, Record


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Attachment
        fields = ['description', 'attachment', 'attachment_type', 'id']


class RecordSerializer(serializers.ModelSerializer):

    next_visit_date = serializers.DateField(format='%d.%m.%Y', input_formats=['%d.%m.%Y'])

    class Meta:

        model = Record
