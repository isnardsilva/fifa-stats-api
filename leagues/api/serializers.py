from rest_framework.serializers import ModelSerializer
from leagues.models import League


class LeagueSerializar(ModelSerializer):
    class Meta:
        model = League
        fields = ['id', 'logo_url', 'name', 'country']