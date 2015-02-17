# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from records.serializers import AttachmentSerializer, RecordSerializer
from records.models import Record, Attachment


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
            record = get_object_or_404(Record, pk=record_pk)
            attachment = serializer.save(doctor=request.user, record=record)

            data = {'attachment': serializer.data}
            return Response(data, status=status.HTTP_200_OK)
        
        else:
            data = {
                'errors': serializer.errors
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class RecordsApiView(APIView):

    def post(self, request, **kwargs):

        serializer = RecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'record': serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
