from product.models.item import Item
from product.models.cart import Cart, CartItem
from rest_framework import viewsets
from product.serializers.cart import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset =  Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset =  CartItem.objects.all()
    serializer_class = CartItemSerializer