from drf_yasg import openapi
from rest_framework import serializers
from .models import ShoppingBasket

class ShoppingBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingBasket
        fields = '__all__'