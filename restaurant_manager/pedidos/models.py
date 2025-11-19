from django.db import models
from products.models import Product

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('preparando', 'Preparando'),
        ('finalizado', 'Finalizado'),
    ]

    nome_cliente = models.CharField(max_length=255, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')

    def __str__(self):
        return f"Pedido #{self.id} - {self.nome_cliente}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"