# backend/cart/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet

router = DefaultRouter()
router.register(r'cart', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', CartItemViewSet.as_view({'post': 'add_to_cart'}), name='add-to-cart'),
]
