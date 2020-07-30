from rest_framework.serializers import ModelSerializer
from leagues.models import League
from nationalities.api.serializers import NationalitySerializer


class LeagueSerializar(ModelSerializer):
    country = NationalitySerializer()

    class Meta:
        model = League
        fields = ['id', 'logo_url', 'name', 'division', 'country']