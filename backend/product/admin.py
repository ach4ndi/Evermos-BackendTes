from django.contrib import admin

# Register your models here.
from product.models.item import Item
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'stock', 'price', 'description', 'user_create')

admin.site.register(Item, ItemAdmin)