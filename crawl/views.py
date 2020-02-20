from rest_framework import viewsets, permissions, filters
from patients.serializers import PatientSerializer
from rest_framework.response import Response
from .crawler import Crawler


class CrawlViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response()

    def create(self, request):
        update = Crawler().get()
        return Response(update)

