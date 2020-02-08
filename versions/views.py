from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from coronainfo.permissions import IsAdminOrReadOnly
from .serializers import VersionSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = VersionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-date"
