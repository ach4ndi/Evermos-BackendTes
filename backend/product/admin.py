from django.contrib import admin

# Register your models here.
from product.models.item import Item
from product.models.cart import Cart, CartItem
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'stock', 'price', 'description', 'user_create')

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('user', 'is_checkout', 'total_price', 'created_at')

class CartItemdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ('cart', 'item', 'quantity', 'total_price', 'created_at')

admin.site.register(Item, ItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemdmin)