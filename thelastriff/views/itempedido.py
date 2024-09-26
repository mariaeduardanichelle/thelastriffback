from rest_framework.viewsets import ModelViewSet

from thelastriff.models import ItemPedido
from thelastriff.serializers import ItemPedidoSerializer

from rest_framework.permissions import IsAuthenticated

class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    permission_classes = [IsAuthenticated]