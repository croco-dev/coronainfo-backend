from rest_framework import viewsets, filters
from .serializers import NoticeSerializer
from rest_framework.response import Response
from .models import Notice


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-date"]

    def list(self, request, *args, **kwargs):
        notice = Notice.objects.first()
        if notice is None:
          return Response('공지사항이 없습니다.',status=404)
        serializer = NoticeSerializer(data=notice.__dict__)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
