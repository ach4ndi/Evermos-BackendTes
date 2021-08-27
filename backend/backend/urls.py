"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from product.views.item import ItemViewSet, ItemDetailViewSet
from product.views.cart import CartViewSet, CartDetailViewSet,CartItemViewSet

API_PREFIX = 'api'

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('{}/item/'.format(API_PREFIX), ItemDetailViewSet.as_view({'get': 'list'})),
    path('{}/item/<int:pk>'.format(API_PREFIX), ItemViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })),
    path('{}/cart/'.format(API_PREFIX), CartDetailViewSet.as_view({'get': 'list'})),
    path('{}/cart/<int:pk>'.format(API_PREFIX), CartViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })),
]