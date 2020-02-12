from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from coronainfo.permissions import IsAdminOrReadOnly
from .models import Version
from .serializers import VersionSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-created_at"
