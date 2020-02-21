from django.db import models

# Create your models here.
class Notice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
