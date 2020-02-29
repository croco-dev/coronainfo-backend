from rest_framework import serializers
from movements.serializers import MovementSerializer
from .models import Patient, PatientLocation


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = []


class PatientReportSerializer(serializers.Serializer):
    total_report = serializers.ListField()
    cure_report = serializers.ListField()
    death_report = serializers.ListField()

class PatientLocationSerializer(serializers.ModelSerializer):
    class Meta:
      model = PatientLocation
      exclude = []