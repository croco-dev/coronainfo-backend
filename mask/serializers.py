# 모델 설정 fields = ('id','title','genre','year') # 필드 설정
from rest_framework import serializers


class MaskSerializer(serializers.Serializer):
  code = serializers.CharField()
  name = serializers.CharField()
  type = serializers.CharField()
  add = serializers.CharField()
  tel = serializers.CharField()
  stock_est = serializers.CharField()
  stock_d = serializers.CharField()
  stock_t = serializers.CharField()
  stock_cnt = serializers.IntegerField()
  sold_cnt = serializers.IntegerField()
  remain_cnt = serializers.IntegerField()
  lat = serializers.FloatField()
  lng = serializers.FloatField()
  creat_time = serializers.CharField()
