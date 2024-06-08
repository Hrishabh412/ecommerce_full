# backend/cart/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(product=product)
        
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        
        cart_item.save()
        serializer = self.get_serializer(cart_item)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
