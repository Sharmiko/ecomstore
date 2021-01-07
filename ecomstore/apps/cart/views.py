from rest_framework import viewsets

from ecomstore.apps.cart.mixins import ShowCartMixin, AddToCartMixin


class CartViewSet(ShowCartMixin,
                  AddToCartMixin,
                  viewsets.ViewSet):
    # TODO - add permission classes
    pass
