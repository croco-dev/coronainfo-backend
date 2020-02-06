from django.db import models
from patients.models import Patient


class Movement(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=20)
    lat = models.IntegerField()
    lng = models.IntegerField()
    patient = models.ForeignKey(
        Patient, related_name="movements", on_delete=models.CASCADE
    )

