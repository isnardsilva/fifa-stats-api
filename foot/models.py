from django.db import models

# Create your models here.
class Foot(models.Model):
    side = models.CharField(max_length=50)

    def __str__(self):
        return self.side