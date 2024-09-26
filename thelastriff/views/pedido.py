from rest_framework.viewsets import ModelViewSet

from thelastriff.models import Pedido
from thelastriff.serializers import PedidoSerializer

from rest_framework.permissions import IsAuthenticated

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]