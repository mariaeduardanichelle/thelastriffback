from rest_framework.viewsets import ModelViewSet

from thelastriff.models import Guitarra
from thelastriff.serializers import GuitarraSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated


class GuitarraViewSet(ModelViewSet):
    queryset = Guitarra.objects.all()
    serializer_class = GuitarraSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
