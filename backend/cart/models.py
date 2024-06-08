# backend/cart/models.py

from django.db import models
from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
