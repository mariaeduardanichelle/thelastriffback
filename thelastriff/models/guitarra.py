from django.db import models
from uploader.models import Image

class Guitarra(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.marca} ({self.modelo})"