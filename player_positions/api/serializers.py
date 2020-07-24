from rest_framework.serializers import ModelSerializer
from player_positions.models import PlayerPosition

class PlayerPositionSerializer(ModelSerializer):
    class Meta:
        model = PlayerPosition
        fields = ['id', 'name']