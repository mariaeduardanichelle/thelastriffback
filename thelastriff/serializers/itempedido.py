from rest_framework.serializers import ModelSerializer

from thelastriff.models import ItemPedido
from thelastriff.serializers.guitarra import GuitarraSerializer
from thelastriff.serializers.pedido import PedidoSerializer

class ItemPedidoSerializer(ModelSerializer):
    guitarra = GuitarraSerializer()
    pedido = PedidoSerializer()

    class Meta:
        model = ItemPedido
        fields = ['id', 'pedido', 'guitarra', 'quantidade']