from django.db import models

from django.utils.translation import gettext as _

class ItemPedido(models.Model):
    pedido = models.ForeignKey('thelastriff.Pedido', on_delete=models.CASCADE)
    guitarra = models.ForeignKey('thelastriff.Guitarra', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return _(f"{self.quantidade}x {self.guitarra.modelo} no pedido {self.pedido.id}")
    