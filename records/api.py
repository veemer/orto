# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from records.serializers import AttachmentSerializer, RecordSerializer
from records.models import Record, Attachment, Patient


class AttachmentsApiView(APIView):

    parser_classes = (FileUploadParser,)

    def get(self, request, **kwargs):

        record_pk = kwargs.get('record_pk')
        attachments = Attachment.objects.filter(record_id=record_pk)
        serialized = AttachmentSerializer(attachments, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):

        serializer = AttachmentSerializer(data=request.data)

        if serializer.is_valid():

            record_pk = kwargs.get('record_pk')
            if record_pk:
                record = get_object_or_404(Record, pk=record_pk)
            else:
                patient_id = request.POST.get('patient_id')
                patient = get_object_or_404(Patient, id=patient_id)
                record = Record.objects.create(doctor=request.user, patient=patient)

            attachment = serializer.save(doctor=request.user, record=record)

            record = RecordSerializer(record)

            data = {'attachment': serializer.data, 'record': record.data}
            return Response(data, status=status.HTTP_200_OK)
        
        else:
            data = {
                'errors': serializer.errors
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class RecordsApiView(APIView):

    def get(self, request, **kwargs):

        record_pk = self.kwargs.get('record_pk')
        record = get_object_or_404(Record, id=record_pk)
        serialized = RecordSerializer(record)

        return Response({'record': serialized.data}, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):

        record_pk = self.kwargs.get('record_pk')

        if record_pk is not None:
            record = get_object_or_404(Record, id=record_pk)
            serializer = RecordSerializer(record, data=request.data)
        else:
            serializer = RecordSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'record': serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
