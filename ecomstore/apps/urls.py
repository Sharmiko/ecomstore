from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ecomstore.apps.catalog.urls')),
    path('api/', include('ecomstore.apps.cart.urls')),
]

