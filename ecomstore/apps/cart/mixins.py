from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from ecomstore.apps.cart.utils import _cart_id
from ecomstore.apps.cart.models import CartItem
from ecomstore.apps.cart.serializers import CartItemSerializer

from ecomstore.apps.catalog.models import Product


class ShowCartMixin(object):

    @action(detail=False, methods=['GET'])
    def get_cart(self, request):
        """ show cart based on `cart_id`
        """
        cart_id = request.query_params.get('cart_id')
        if not cart_id:
            return Response(
                {
                    'message': 'Cart id was not provided',
                    'status': 'error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        cart_item = CartItem.objects.filter(cart_id=cart_id)
        if not cart_item:
            return Response(
                {
                    'message': 'Cart item with provided cart id was not found',
                    'status': 'error'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CartItemSerializer(cart_item, many=True)

        return Response(
            {
                'cart': serializer.data
            },
            status=status.HTTP_200_OK
        )


class AddToCartMixin(object):

    @action(detail=False, methods=['POST'])
    def add_to_cart(self, request):
        data = request.data

        cart_id = data.get('cart_id')
        quantity = data.get('quantity')
        product_uuid = data.get('product_uuid')

        if not cart_id:
            return Response(
                {
                    'message': 'Cart ID was not provided',
                    'status': 'error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not quantity:
            return Response(
                {
                    'message': 'Product quantity was not provided',
                    'status': 'error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not product_uuid:
            return Response(
                {
                    'message': 'Product UUID was not provided',
                    'status': 'error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        product = Product.objects.filter(uuid=product_uuid).first()
        if not product:
            return Response(
                {
                    'message': 'Product with provided UUID was not found',
                    'status': 'error'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        new_item = CartItem(cart_id=cart_id, quantity=quantity,
                            product=product)
        new_item.save()
        return Response(
            {
                'message': 'Item added successfully',
                'status': 'success'
            },
            status=status.HTTP_200_OK
        )
