from django.db import models
from patients.models import Patient


class Movement(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, on_update=models.CASCADE)

    def __str__(self):
        return self.address
