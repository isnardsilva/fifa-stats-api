from rest_framework.serializers import ModelSerializer
from nationalities.models import Nationality


class NationalitySerializer(ModelSerializer):
    class Meta:
        model = Nationality
        fields = ['id', 'name']