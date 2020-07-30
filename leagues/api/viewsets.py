from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from leagues.models import League
from .serializers import LeagueSerializar


class LeagueViewSet(ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializar
    filter_backends = [SearchFilter]
    search_fields = ['name']