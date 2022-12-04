from django.shortcuts import get_object_or_404, render
from shoppingBasket.models import User
from shoppingBasket.models import ShoppingBasket
from .serializers import ShoppingBasketSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


class ShoppingBasketViewSet(viewsets.ViewSet):
    def list(self, request): # GET /api/shoppingBasket
        queryset = ShoppingBasket.objects.all()
        serializer = ShoppingBasketSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None): # GET /api/shoppingBasket/:id
        queryset = ShoppingBasket.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ShoppingBasketSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Create a shopping basket", responses={404: 'slug not found'})
    def create(self, request): # POST /api/shoppingBasket
        serializer = ShoppingBasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None): # PUT /api/shoppingBasket/:id
        shoppingBasket = ShoppingBasket.objects.get(pk=pk)
        serializer = ShoppingBasketSerializer(shoppingBasket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # DELETE /api/shoppingBasket/:id
        shoppingBasket = ShoppingBasket.objects.get(pk=pk)
        shoppingBasket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk=None):
        shoppingBasket = ShoppingBasket.objects.get(pk=pk)
        serializer = ShoppingBasketSerializer(shoppingBasket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        