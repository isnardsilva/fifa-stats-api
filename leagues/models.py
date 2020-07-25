from django.db import models
from nationalities.models import Nationality

# Create your models here.
class League(models.Model):
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
