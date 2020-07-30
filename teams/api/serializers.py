from rest_framework.serializers import ModelSerializer
from teams.models import Team
from leagues.api.serializers import LeagueSerializar


class TeamSerializer(ModelSerializer):
    league = LeagueSerializar()

    class Meta:
        model = Team
        fields = ['id', 'logo_url', 'name', 'league']