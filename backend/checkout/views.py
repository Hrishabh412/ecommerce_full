# backend/checkout/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def checkout(request):
    # In a real application, you would handle order creation, payment processing, etc.
    # For this dummy checkout, we simply return a success message.
    return Response({"message": "Checkout successful!"}, status=status.HTTP_200_OK)
