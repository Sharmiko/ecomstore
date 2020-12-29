from rest_framework.serializers import ModelSerializer

from ecomstore.apps.cart.models import CartItem


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart_id', 'date_added', 'quantity', 'product', )
