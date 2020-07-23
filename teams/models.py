from django.db import models
from leagues.models import League

# Create your models here.
class Team(models.Model):
    logo_url = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

