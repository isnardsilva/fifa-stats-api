from rest_framework.viewsets import ModelViewSet
from foot.models import Foot
from .serializers import FootSerializer


class FootViewSet(ModelViewSet):
    queryset = Foot.objects.all()
    serializer_class = FootSerializer