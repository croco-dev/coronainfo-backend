from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from .serializers import PatientSerializer, PatientReportSerializer
from .models import Patient
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count
from feeds.models import Feed
from django.core.cache import cache


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-index"
    def list(self, request):
        cached_patients = cache.get('patients', None)
        if not cached_patients:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            cache.set('patients', serializer.data, 60 * 60)
            cached_patients = serializer.data
        return Response(cached_patients)
    def retrieve(self, request, pk=None):
        patient = Patient.objects.filter(index=pk).first()
        if patient is None:
          return Response('Data null', status=404)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def perform_create(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "patient"
        data["date"] = data["last_update"]
        feeds_serializer = FeedsSerializer(data=data)
        if feeds_serializer.is_valid():
            feeds_serializer.save()
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "patient"
        data["date"] = data["last_update"]
        feeds_serializer = FeedsSerializer(data=data)
        if feeds_serializer.is_valid():
            feeds_serializer.save()
        return super().perform_update(serializer)

class PatientReportViewSet(viewsets.ModelViewSet):
        serializer_class = PatientReportSerializer
        def list(self, request):
            data = {}
            data["total_report"] = Patient.objects.all().values('date').annotate(total=Count('date')).order_by('date')
            data["cure_report"] = Feed.objects.filter(status='완치').values('date').annotate(total=Count('date')).order_by('date')
            data["death_report"] = Feed.objects.filter(status='사망').values('date').annotate(total=Count('date')).order_by('date')
            serializer = PatientReportSerializer(data=data)
            if serializer.is_valid():
              return Response(serializer.data)
            else:
              return Response(serializer.errors)