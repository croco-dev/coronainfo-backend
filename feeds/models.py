from django.db import models


class Feed(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=200, blank=True)
    contact_count = models.IntegerField(blank=True)
    second_infection = models.IntegerField(blank=True, null=True)
    lat = models.IntegerField(blank=True)
    lng = models.IntegerField(blank=True)
    index = models.IntegerField()
    log_type = models.CharField(max_length=10)
