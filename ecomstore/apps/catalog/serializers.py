from rest_framework.serializers import ModelSerializer

from ecomstore.apps.catalog.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

