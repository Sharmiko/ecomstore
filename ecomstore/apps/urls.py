from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ecomstore.apps.cart.views import CartViewSet
from ecomstore.apps.catalog.views import CategoryViewSet, ProductViewSet
from ecomstore.apps.checkout.views import CreditCartViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, r'categories')
router.register(r'product', ProductViewSet, r'product')
router.register(r'cart', CartViewSet, r'cart')
router.register(r'cc', CreditCartViewSet, r'cc')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
