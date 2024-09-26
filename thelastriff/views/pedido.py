from rest_framework.viewsets import ModelViewSet

from thelastriff.models import Pedido
from thelastriff.serializers import PedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer