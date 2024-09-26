from django.db import models

from django.conf import settings

from django.utils.translation import gettext as _

class Pedido(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return _(f"Pedido {self.id} - Cliente: {self.cliente.username}")

