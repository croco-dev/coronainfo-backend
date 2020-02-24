from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-index"
    def retrieve(self, request, pk=None):
        queryset = Patient.objects.all()
        patient = get_object_or_404(queryset, index=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

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
