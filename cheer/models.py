from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Cheer(models.Model):
  ip = models.GenericIPAddressField()
  content = models.TextField()
  tags = ArrayField(models.CharField(max_length=200),blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
