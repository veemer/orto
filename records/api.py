# -*- coding: utf-8 -*-

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        print request.data.keys()
        # ...
        # do some staff with uploaded file
        # ...
        return Response(status=204)
