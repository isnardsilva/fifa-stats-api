from rest_framework.serializers import ModelSerializer
from foot.models import Foot


class FootSerializer(ModelSerializer):
    class Meta:
        model = Foot
        fields = ['id', 'side']