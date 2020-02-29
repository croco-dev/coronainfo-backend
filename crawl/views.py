from rest_framework import viewsets, permissions, filters
from versions.serializers import VersionSerializer
from rest_framework.response import Response
from .crawler import Crawler


class CrawlViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response()

    def create(self, request):
        update = Crawler().get()
        # update = Crawler().seoul()
        serializer = VersionSerializer(data=update.__dict__)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TempCrawlViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response()

    def create(self, request):
        update = Crawler().temp()
        serializer = VersionSerializer(data=update.__dict__)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

