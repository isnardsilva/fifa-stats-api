from rest_framework.viewsets import ModelViewSet
from nationalities.models import Nationality
from .serializers import NationalitySerializer


class NationalityViewSet(ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer