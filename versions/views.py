from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from coronainfo.permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from .models import Version
from .serializers import VersionSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-date"

    def list(self, request):
        versionSerializer = VersionSerializer(
            Version.objects.order_by("-date").first()
        )
        return Response(versionSerializer.data)

    def perform_create(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = ""
        versionSerializer = VersionSerializer(data=data)
        if versionSerializer.is_valid():
            versionSerializer.save()
        return super().perform_create(versionSerializer)

    def perform_update(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "patient"
        versionSerializer = VersionSerializer(data=data)
        if versionSerializer.is_valid():
            versionSerializer.save()
        return super().perform_update(versionSerializer)
