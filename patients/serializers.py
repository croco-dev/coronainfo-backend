# 모델 설정 fields = ('id','title','genre','year') # 필드 설정
from rest_framework import serializers
from movements.serializers import MovementSerializer
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    movements = MovementSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        exclude = []
