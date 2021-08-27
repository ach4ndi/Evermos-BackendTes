from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(default=0, decimal_places=1, max_digits=11)
    description = models.CharField(max_length=500)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items_user_create', blank=False)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '{} / {}'.format(self.user_create.username, self.name)

    def __str__(self):
        return '{} / {}'.format(self.user_create.username, self.name)
