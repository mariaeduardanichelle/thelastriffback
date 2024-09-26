from rest_framework.viewsets import ModelViewSet

from thelastriff.models import ItemPedido
from thelastriff.serializers import ItemPedidoSerializer

class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer