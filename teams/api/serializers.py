from rest_framework.serializers import ModelSerializer
from teams.models import Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'logo_url', 'name']