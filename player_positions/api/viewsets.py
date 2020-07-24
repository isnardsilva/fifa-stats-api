from rest_framework.viewsets import ModelViewSet
from player_positions.models import PlayerPosition
from .serializers import PlayerPositionSerializer


class PlayerPositionViewSet(ModelViewSet):
    queryset = PlayerPosition.objects.all()
    serializer_class = PlayerPositionSerializer
