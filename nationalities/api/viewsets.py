from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from nationalities.models import Nationality
from .serializers import NationalitySerializer


class NationalityViewSet(ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']