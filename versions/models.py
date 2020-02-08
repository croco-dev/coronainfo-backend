from django.db import models


class Version(models.Model):
    created_at = models.DateField()
    date = models.DateField()
    version = models.TextField(max_length=50)

