from django.db import models

# Create your models here.
class League(models.Model):
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)