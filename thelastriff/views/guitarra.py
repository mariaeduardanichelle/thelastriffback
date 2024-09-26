from rest_framework.viewsets import ModelViewSet

from thelastriff.models import Guitarra
from thelastriff.serializers import GuitarraSerializer

class GuitarraViewSet(ModelViewSet):
    queryset = Guitarra.objects.all()
    serializer_class = GuitarraSerializer