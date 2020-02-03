from django.db import models


class Patient(models.Model):
    index = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=30)
    contact_count = models.IntegerField()
    second_infection = models.IntegerField()

    def __str__(self):
        return "%s %s %s %s" % (self.index, self.date, self.status, self.contact_count)
