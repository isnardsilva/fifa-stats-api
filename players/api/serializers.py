from rest_framework.serializers import ModelSerializer
from players.models import Player
from teams.api.serializers import TeamSerializer

class PlayerSerializer(ModelSerializer):
    club = TeamSerializer()

    class Meta:
        model = Player
        fields = ['id', 'short_name', 'nationality', 'club', 'overall']
