# 모델 설정 fields = ('id','title','genre','year') # 필드 설정
from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    news = serializers.ListField()
    total = serializers.IntegerField()

