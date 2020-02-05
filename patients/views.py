from rest_framework import viewsets, permissions
from .serializers import PatientSerializer
from .models import Patient


class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        permission_classes = [permissions.IsAuthenticated]
        return super().create(request, *args, **kwargs)
