from django.db import models

# Create your models here.

class Cheer(models.Model):
  ip = models.GenericIPAddressField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
