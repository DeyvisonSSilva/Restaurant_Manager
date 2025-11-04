from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Comida'),
        ('drink', 'Bebida'),
        ('dessert', 'Sobremesa'),
        ('other', 'Outro'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nome do produto")
    description = models.TextField(blank=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Categoria")
    available = models.BooleanField(default=True, verbose_name="Disponível")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    def __str__(self):
        return self.name
