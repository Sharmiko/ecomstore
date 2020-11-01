from django.urls import path

from ecomstore.apps.catalog.views import CategoryList

urlpatterns = [
    path('categories/', CategoryList.as_view())
]

