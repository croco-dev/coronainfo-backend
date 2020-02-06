from rest_framework import viewsets
from .serializers import FeedsSerializer
from .models import Feed


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedsSerializer
    ordering_fields = ["id"]

