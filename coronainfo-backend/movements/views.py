from rest_framework import viewsets
from .serializers import MovementSerializer
from .models import Movement


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

    def perform_create(self, serializer):
        serializer.save()
