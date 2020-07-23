from rest_framework.viewsets import ModelViewSet
from leagues.models import League
from .serializers import LeagueSerializar


class LeagueViewSet(ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializar