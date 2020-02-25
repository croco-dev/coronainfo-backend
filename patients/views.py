from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from .serializers import PatientSerializer, PatientReportSerializer
from .models import Patient
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count


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

class PatientReportViewSet(viewsets.ModelViewSet):
        serializer_class = PatientReportSerializer
        def list(self, request):
            data = {}
            data["total_report"] = Patient.objects.all().values('date').annotate(total=Count('date')).order_by('date')
            data["cure_report"] = Patient.objects.filter(status='완치').values('date').annotate(total=Count('date')).order_by('date')
            data["death_report"] = Patient.objects.filter(status='사망').values('date').annotate(total=Count('date')).order_by('date')
            serializer = PatientReportSerializer(data=data)
            if serializer.is_valid():
              return Response(serializer.data)
            else:
              return Response(serializer.errors)