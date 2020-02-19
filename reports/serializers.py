# 모델 설정 fields = ('id','title','genre','year') # 필드 설정
from rest_framework import serializers


class ReportSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    cure_count = serializers.IntegerField()
    death_count = serializers.IntegerField()
    increase_count = serializers.IntegerField()
    contact_count = serializers.IntegerField()
    second_rate = serializers.IntegerField()
    cure_rate = serializers.IntegerField()

