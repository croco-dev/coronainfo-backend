from rest_framework import viewsets, filters
from .serializers import FeedsSerializer
from .models import Feed


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedsSerializer

    filter_backends = [filters.OrderingFilter]

    ordering = "-date"

