from django.db import models
from nationalities.models import Nationality
from teams.models import Team
from foot.models import Foot
from player_positions.models import PlayerPosition

# Create your models here.
class Player(models.Model):
    photo_url = models.CharField(max_length=300, default='https://cdn.sofifa.com/players/notfound_0_240.png', blank=True)
    short_name = models.CharField(max_length=300)
    long_name = models.CharField(max_length=300)
    date_of_birth = models.DateField('Date of Birth')
    height_cm = models.IntegerField()
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=False)
    club = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    overall = models.IntegerField()
    preferred_foot = models.ForeignKey(Foot, on_delete=models.CASCADE, null=False)
    player_positions = models.ManyToManyField(PlayerPosition, related_name='player_positions')
    team_position = models.ForeignKey(PlayerPosition, related_name='team_position', on_delete=models.CASCADE, null=False)
    team_jersey_number = models.IntegerField()

    def __str__(self):
        return self.short_name




