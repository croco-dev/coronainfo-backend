from rest_framework import viewsets, filters
from feeds.serializers import FeedsSerializer
from .serializers import MovementSerializer
from rest_framework.response import Response
from .models import Movement


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-date"

    def perform_create(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "movements"
        feedsSerializer = FeedsSerializer(data=data)
        if feedsSerializer.is_valid():
            feedsSerializer.save()
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        data = self.request.data
        data._mutable = True
        data["log_type"] = "movements"
        feedsSerializer = FeedsSerializer(data=data)
        if feedsSerializer.is_valid():
            feedsSerializer.save()
        return super().perform_update(serializer)
