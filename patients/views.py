from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
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
        feeds_serializer = FeedsSerializer(data=data)
        if feeds_serializer.is_valid():
            feeds_serializer.save()
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "patient"
        feeds_serializer = FeedsSerializer(data=data)
        if feeds_serializer.is_valid():
            feeds_serializer.save()
        return super().perform_update(serializer)
