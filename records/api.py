# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from records.serializers import AttachmentSerializer
from records.models import Record, Attachment


class AttachmentsApiView(APIView):

    parser_classes = (FileUploadParser,)

    def post(self, request, **kwargs):

        serializer = AttachmentSerializer(data=request.data)

        if serializer.is_valid():

            record_pk = kwargs.get('record_pk')
            record = get_object_or_404(Record, pk=record_pk)
            attachment = serializer.save(doctor=request.user, record=record)

            data = {'attachment': serializer.data}
            return Response(data, status=200)
        
        else:
            data = {
                'errors': serializer.errors
            }

            return Response(data, status=400)
