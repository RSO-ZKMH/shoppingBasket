from django.shortcuts import get_object_or_404
from django.http import Http404
from shoppingBasket.models import ShoppingBasket
from .serializers import ShoppingBasketSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema
from constance import config
from constance.signals import config_updated
from django.dispatch import receiver

# Create your views here.


class ShoppingBasketViewSet(viewsets.ViewSet):

    
    def addProduct(self, request):
        serializer = ShoppingBasketSerializer(data=request.data)
        
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        userId = serializer.data.get('userId')
        productIds = serializer.data.get('productIds')

        # Get first basket with userId
        shoppingBasket = ShoppingBasket.objects.filter(userId=userId).first()
        
        if not shoppingBasket:
            # create basket
            basket = ShoppingBasket(userId=userId, productIds=productIds)
            basket.save()
            return JsonResponse(basket, status=status.HTTP_200_OK, safe=False)
        else:
            # update basket
            if(productIds not in shoppingBasket.productIds):
                print(productIds)
                shoppingBasket.productIds.extend(productIds)
                shoppingBasket.save()
                return JsonResponse(shoppingBasket, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse({'error': 'Product already in shopping basket'}, status=status.HTTP_400_BAD_REQUEST)
        
        


        