from product.models.item import Item
from rest_framework import viewsets
from product.serializers.item import ItemSerializer, ItemDetailSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset =  Item.objects.all()
    serializer_class = ItemSerializer
    #permission_classes = [
    #    permissions.IsAuthenticated,
    #]

class ItemDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Item.objects.all()
    serializer_class = ItemDetailSerializer