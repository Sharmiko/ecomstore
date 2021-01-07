from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ecomstore.apps.cart.views import ShowCartViewSet
from ecomstore.apps.catalog.views import CatalogViewSet


router = DefaultRouter()
router.register(r'catalog', CatalogViewSet, r'catalog')
router.register(r'cart', ShowCartViewSet, r'cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
