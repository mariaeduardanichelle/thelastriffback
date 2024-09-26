from django.db import models

class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"
