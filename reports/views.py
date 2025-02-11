from django.db.models import Sum
from rest_framework import viewsets, permissions, filters
from feeds.serializers import FeedsSerializer
from rest_framework.response import Response
from patients.models import Patient, PatientLocation
from versions.models import Version
import datetime
from .serializers import ReportSerializer
from .models import Report
from patients.serializers import PatientLocationSerializer
class ReportViewSet(viewsets.ViewSet):
    serializer_class = ReportSerializer

    def list(self, request):
        data = {}
        report = Report.objects.order_by("-date").first()
        data["total_count"] = report.patient_count
        data["death_count"] = report.death_count
        data["cure_count"] = report.cure_count
        today = Version.objects.order_by("-date").first().date
        yesterday_count = Patient.objects.filter(
            date=today - datetime.timedelta(days=1)
        ).count()
        today_count = Patient.objects.filter(date=today).count()
        data["increase_count"] = today_count
        data["contact_count"] = Patient.objects.aggregate(Sum("contact_count"))[
            "contact_count__sum"
        ]
        second_count = Patient.objects.filter(second_infection__isnull=False).count()
        data["second_rate"] = round((second_count / data["total_count"]) * 100)
        data["cure_rate"] = round((data["cure_count"] / data["total_count"]) * 100)
        total_location = PatientLocationSerializer(PatientLocation.objects.order_by('-total').first())
        increase_location = PatientLocationSerializer(PatientLocation.objects.order_by('-increase').first())
        data["top_rate_increase_location"] = increase_location.data
        data["top_rate_total_location"] = total_location.data
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
