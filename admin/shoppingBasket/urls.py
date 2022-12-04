from django.contrib import admin
from django.urls import path

from shoppingBasket.views import ShoppingBasketViewSet
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Shopping Basket API",
        default_version='1.0.0',
        description="API Documentation for shopping basket",
    ),
    public=True
)

urlpatterns = [
    path('shoppingBasket', ShoppingBasketViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('shoppingBasket/<str:pk>', ShoppingBasketViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
        'patch': 'partial_update',
    })),
    path('swagger/schema', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
