from django.db import models

class ItemPedido(models.Model):
    pedido = models.ForeignKey('thelastriff.Pedido', on_delete=models.CASCADE)
    guitarra = models.ForeignKey('thelastriff.Guitarra', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.guitarra.modelo} no pedido {self.pedido.id}"
    