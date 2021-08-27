from product.models.item import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' #menampilkan semua field pada class Album