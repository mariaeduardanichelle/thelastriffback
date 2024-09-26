from django.contrib import admin
from .models import Guitarra, Pedido, ItemPedido

@admin.register(Guitarra)
class GuitarraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'preco', 'estoque')
    search_fields = ('marca', 'modelo')
    list_filter = ('marca', 'modelo')
    ordering = ('marca', 'modelo', 'preco')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_pedido')  
    search_fields = ('id',)
    list_filter = ('data_pedido',)
    ordering = ('data_pedido', 'id')

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'guitarra', 'quantidade')
    search_fields = ('pedido__id', 'guitarra__modelo')
    list_filter = ('pedido', 'guitarra')
    ordering = ('pedido', 'guitarra')