from rest_framework import viewsets
from django.shortcuts import get_object_or_404, render
from .serializers import CheerSerializer
from .models import Cheer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class CheerViewSet(viewsets.ModelViewSet):
    queryset = Cheer.objects.all()
    serializer_class = CheerSerializer
    permission_classes = [AllowAny,]
    def create(self, request):
        request.data["ip"] = request.META.get('REMOTE_ADDR')
        count = Cheer.objects.filter(ip=request.META.get('REMOTE_ADDR')).count()
        if count > 0:
          return Response('only one cheer', status=400)
        return super().create(request)