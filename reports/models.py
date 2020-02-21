from django.db import models


class Report(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    patient_count = models.IntegerField()
    cure_count = models.IntegerField()
    death_count = models.IntegerField()

