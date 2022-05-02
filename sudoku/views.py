from io import BytesIO

import requests
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from xhtml2pdf import pisa

from sudoku.models import Sudoku
from sudoku.serializers import SudokuSerializer


class SudokuViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin):
    queryset = Sudoku.objects.all()
    serializer_class = SudokuSerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = queryset.all().exclude(owner=self.request.user)
        elif self.action == 'own':
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        task = get_object_or_404(Sudoku.objects.filter(pk=kwargs['pk']))
        task.delete()
        return Response({"detail": "Sudoku deleted"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'], url_path='own')
    def own(self, request, *args, **kwargs):
        return super().list(request)

    @action(detail=False, methods=['POST'], url_path='pdf')
    def pdf(self, request, *args, **kwargs):
        template = get_template('template.html')
        html = template.render({'context': 'context'})
        result = BytesIO()
        pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

        file = NamedTemporaryFile(suffix='.pdf')
        filename = file.name
        file.write(result.getvalue())
        file.seek(0)

        files = {'file': open(filename, 'rb')}
        response = requests.post(FILESERVICE, files=files)
        pdf_url = response.json().get('url')
        print(pdf_url)
        return Response(pdf_url)
