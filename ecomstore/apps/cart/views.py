from rest_framework import status, viewsets
from rest_framework.response import Response

from ecomstore.apps.cart.utils import _cart_id
from ecomstore.apps.cart.models import CartItem
from ecomstore.apps.cart.serializers import CartItemSerializer

from ecomstore.apps.catalog.models import Product


class ShowCartViewSet(viewsets.ViewSet):

    def list(self, request):
        cart_id = request.query_params.get('cart_id')
        if not cart_id:
            return Response(
                {
                    'message': 'Cart id was not provided',
                    'status': 'error'
                }, status=status.HTTP_400_BAD_REQUEST)

        cart_item = CartItem.objects.filter(cart_id=cart_id).first()
        if not cart_item:
            return Response(
                {
                    'message': 'Cart item with provided cart id was not found',
                    'status': 'error'
                }, status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(cart_item)

        return Response({'cart': serializer.data})


    def create(self, request):
        data = request.data

        cart_id = data.get('cart_id')
        quantity = data.get('quantity')
        product_uuid = data.get('product_uuid')

        if not quantity:
            return Response(
                {
                    'message': 'Product quantity was not provided',
                    'status': 'error'
                }, status=status.HTTP_400_BAD_REQUEST)
        if not product_uuid:
            return Response(
                {
                    'message': 'Product UUID was not provided',
                    'status': 'error'
                }, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.filter(uuid=product_uuid).first()
        if not product:
            return Response(
                {
                    'message': 'Product with provided UUID was not found',
                    'status': 'error'
                }, status=status.HTTP_404_NOT_FOUND)

        if not cart_id:
            new_item = CartItem(
                cart_id=_cart_id(request),
                quantity=quantity,
                product=product
            )
            new_item.save()

            return Response(
                {
                    'message': 'Item added successfully',
                    'status': 'success'
                }, status=status.HTTP_200_OK)

        cart_items = CartItem.objects.filter(cart_id=cart_id)
        product_in_cart = False

        for cart_item in cart_items:
            if cart_item.product.uuid == product.uuid:
                cart_item.augment_quantity(quantity)
                product_in_cart = True

        if not product_in_cart:
            new_item = CartItem(
                cart_id=_cart_id(request),
                quantity=quantity,
                product=product
            )
            new_item.save()

        return Response(
            {
                'message': 'Cart updated successfully',
                'status': 'success'
            }, status=status.HTTP_200_OK)

