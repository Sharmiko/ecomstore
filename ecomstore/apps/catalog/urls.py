from django.urls import path

from ecomstore.apps.catalog.views import CategoryList, ProductDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('product/', ProductDetail.as_view())
]

