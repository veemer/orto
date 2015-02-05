# -*- coding: utf-8 -*-

from rest_framework import serializers
from records.models import Attachment

class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Attachment
        fields = ['description', 'attachment']