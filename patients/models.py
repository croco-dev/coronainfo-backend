from django.db import models


class Patient(models.Model):
    index = models.IntegerField()
    date = models.DateField(null=True)
    last_update = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=200)
    contact_count = models.IntegerField(blank=True, default=0)
    second_infection = models.IntegerField(blank=True, null=True)
    infected_route = models.CharField(blank=True, max_length=300, null=True)
    hospital = models.CharField(blank=True, max_length=30, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(blank=True, max_length=10, null=True)
    country = models.CharField(blank=True, max_length=30, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.index, self.date, self.status, self.contact_count)

class PatientLocation(models.Model):
      name = models.CharField(max_length=10)
      total = models.IntegerField()
      increase = models.IntegerField()

class PatientLocationFeed(models.Model):
      date = models.DateField(auto_now_add=True)
      name = models.CharField(max_length=10)
      total = models.IntegerField()
      increase = models.IntegerField()