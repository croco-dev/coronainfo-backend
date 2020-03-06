from rest_framework import viewsets, filters
from .serializers import MaskSerializer
from rest_framework.response import Response

class MaskViewSet(viewsets.ViewSet):
    serializer_class = MaskSerializer

    def list(self, request, *args, **kwargs):
        data = [
            {
                "code": "12345678",
                "name": "하늘약국",
                "type": "01",
                "add": "서울시 중구 세종로 xxx",
                "tel": "031-1234-5678",
                "stock_est": "2020-03-09",
                "stock_d": "2020-03-09",
                "stock_t": "08:30",
                "stock_cnt": 100,
                "sold_cnt": 20,
                "remain_cnt": 80,
                "lat": 36.6013053,
                "lng": 127.2995696,
                "creat_time": "08:50",
            },
            {
                "code": "12345679",
                "name": "테스트우체국",
                "type": "02",
                "add": "서울시 중구 세종로 xxx",
                "tel": "031-1234-5678",
                "stock_est": "2020-03-09",
                "stock_d": "2020-03-09",
                "stock_t": "08:30",
                "stock_cnt": 100,
                "sold_cnt": 20,
                "remain_cnt": 80,
                "lat": 36.6013053,
                "lng": 127.2995696,
                "creat_time": "08:50",
            }
            ,
            {
                "code": "12345679",
                "name": "테스트농협",
                "type": "03",
                "add": "서울시 중구 세종로 xxx",
                "tel": "031-1234-5678",
                "stock_est": "2020-03-09",
                "stock_d": "2020-03-09",
                "stock_t": "08:30",
                "stock_cnt": 100,
                "sold_cnt": 20,
                "remain_cnt": 80,
                "lat": 36.6013053,
                "lng": 127.2995696,
                "creat_time": "08:50",
            }
        ]
        serializer = MaskSerializer(data=data, many=True)
        if serializer.is_valid():
          return Response(serializer.data)
        else:
          return Response(serializer.errors)
