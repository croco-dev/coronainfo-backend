# 모델 설정 fields = ('id','title','genre','year') # 필드 설정
from rest_framework import serializers
from movements.serializers import MovementSerializer
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    last_movement = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        exclude = []
    def get_last_movement(self, patient):
        movement = patient.movements.all()
        if (len(movement) > 0):
          return MovementSerializer(movement[0], read_only=True).data

