from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from players.models import Player
from teams.api.serializers import TeamSerializer
from player_positions.api.serializers import PlayerPositionSerializer

class PlayerSerializer(ModelSerializer):
    club = TeamSerializer()

    preferred_foot = serializers.SerializerMethodField()
    team_position = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'short_name', 'long_name', 'date_of_birth', 'height_cm', 'weight_kg', 'nationality', 'club', 'overall', 'preferred_foot', 'team_position', 'team_jersey_number']

    def get_preferred_foot(self, obj):
        return '%s' % (obj.preferred_foot)

    def get_team_position(self, obj):
        return '%s' % (obj.team_position)

