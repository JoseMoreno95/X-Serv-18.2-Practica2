from django.db import models

# Create your models here.
class UrlModel(models.Model):
    longUrl = models.CharField(max_length=128)
