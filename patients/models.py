from django.db import models


class Patient(models.Model):
    index = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=200)
    contact_count = models.IntegerField(default=0)
    lat = models.FloatField(blank=True)
    lng = models.FloatField(blank=True)
    second_infection = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.index, self.date, self.status, self.contact_count)
