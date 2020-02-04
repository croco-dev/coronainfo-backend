# 모델 설정 fields = ('id','title','genre','year') # 필드 설정
from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = []
