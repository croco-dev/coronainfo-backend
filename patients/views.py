from rest_framework import viewsets, permissions, filters
from feeds.serializers import FeedsSerializer
from coronainfo.permissions import IsAdminOrReadOnly
from .serializers import PatientSerializer
from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-index"

    def perform_create(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "patient"
        feedsSerializer = FeedsSerializer(data=data)
        if feedsSerializer.is_valid():
            feedsSerializer.save()
        return super().perform_create(feedsSerializer)

    def perform_update(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "patient"
        feedsSerializer = FeedsSerializer(data=data)
        if feedsSerializer.is_valid():
            feedsSerializer.save()
        return super().perform_update(feedsSerializer)
