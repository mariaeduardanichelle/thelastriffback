from django.db import models

class Categoria(models.Model):
    descricao = models.SlugField(max_length=100)

    def __str__(self):
        return self.descricao
    



