from product.models.item import Item
from rest_framework import serializers
from product.serializers.user import UserSerializer

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','name','stock','price','description','user_create','created_at','update_at','delete_at')

class ItemDetailSerializer(serializers.ModelSerializer):
    user_create = UserSerializer(many=False)
    class Meta:
        model = Item
        fields = ('id','name','stock','price','description','user_create','created_at','update_at','delete_at')