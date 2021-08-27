from product.models.item import Item
from rest_framework import viewsets
from product.serializers.item import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset =  Item.objects.all()
    serializer_class = ItemSerializer
