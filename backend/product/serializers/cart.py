from product.models.cart import Cart, CartItem
from rest_framework import serializers
from product.serializers.user import UserSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'total_price','is_checkout','created_at')

class CartDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Cart
        fields = ('id', 'user', 'total_price','is_checkout','created_at')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'