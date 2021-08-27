from django.db import models
from django.contrib.auth.models import User
from product.models.item import Item
from django.core.exceptions import ValidationError

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user', blank=False)
    total_price = models.DecimalField(default=0, decimal_places=1, max_digits=11)
    is_checkout = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    delete_at = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return '{} - [{} | {}]'.format(self.id, self.user.username, self.is_checkout)

    def __str__(self):
        return '{} - [{} | {}]'.format(self.id, self.user.username, self.is_checkout)
    
    def clean(self):
        cart_item = CartItem.objects.filter(cart=self).order_by('id')
        if self.is_checkout == True:
            check_validated = True
            
            for item in cart_item:
                check_validated = self.validate_checkout(item)
                
                if check_validated == False:
                    break
            
            if check_validated == False:
                raise ValidationError('is cant checkout {}'.format(self.id))
    
    def save(self, *args, **kwargs):
        cart_item = CartItem.objects.filter(cart=self).order_by('id')
        
        for item in cart_item:
            self.total_price += item.total_price
        
        if self.is_checkout == True:
            check_validated = True
            
            for item in cart_item:
                check_validated = self.validate_checkout(item)
                
                if check_validated == False:
                    break
            
            if check_validated == False:
                raise ValidationError('is cant checkout {}'.format(self.id))
            
            # update stock
            if check_validated:
                for item in cart_item:
                    obj = Item.objects.get(id=item.item.id)
                    obj.stock-= item.quantity
                    obj.save()
    
        super(Cart, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        cart_item = CartItem.objects.filter(cart=self).order_by('id')
        
        for item in cart_item:
            self.total_price += item.total_price
        
        if self.is_checkout == True:
            check_validated = True
            
            for item in cart_item:
                check_validated = self.validate_checkout(item)
                
                if check_validated == False:
                    break
            
            if check_validated == False:
                raise ValidationError('is cant checkout {}'.format(self.id))
            
            # update stock
            if check_validated:
                for item in cart_item:
                    obj = Item.objects.get(id=item.item.id)
                    obj.stock-= item.quantity
                    obj.save()
    
        super(Cart, self).update(*args, **kwargs)
    
    def validate_checkout(self, item):
        chart_quantity = item.quantity
        item_stock = item.item.stock
        
        if item_stock < chart_quantity:
            return False
        return True

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_id', blank=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart_item', blank=False)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=1, max_digits=11)
    total_price = models.DecimalField(default=0, decimal_places=1, max_digits=11)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    delete_at = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return '{} - [{}] {}'.format(self.cart.user.username, self.cart.id, self.item.name)

    def __str__(self):
        return '{} - [{}] {}'.format(self.cart.user.username, self.cart.id, self.item.name)
    
    def save(self, *args, **kwargs):
        self.price = self.item.price
        self.total_price = self.quantity * self.price
        
        super(CartItem, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        
        super(CartItem, self).save(*args, **kwargs)