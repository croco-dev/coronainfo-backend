from rest_framework import viewsets, permissions, filters
from feeds.serializers import FeedsSerializer
from rest_framework.response import Response
from patients.models import Patient
from versions.models import Version
import datetime
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = ReportSerializer

    def list(self, request):
        data = {}
        data["total_count"] = Patient.objects.count()
        data["death_count"] = Patient.objects.filter(status="사망").count()
        data["cure_count"] = Patient.objects.filter(status="완치").count()
        today = Version.objects.order_by("-date").first().date
        yesterday_count = Patient.objects.filter(
            date=today - datetime.timedelta(days=1)
        ).count()
        today_count = Patient.objects.filter(date=today).count()
        data["increase_rate"] = round(
            (today_count - yesterday_count) / today_count * 100
        )
        second_count = Patient.objects.filter(second_infection__isnull=False).count()
        data["second_rate"] = round((second_count / data["total_count"]) * 100)
        data["death_rate"] = round((data["death_count"] / data["total_count"]) * 100)
        data["cure_rate"] = round((data["cure_count"] / data["total_count"]) * 100)
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

