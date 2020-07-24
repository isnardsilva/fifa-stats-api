from rest_framework.viewsets import ModelViewSet
from players.models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer