from rest_framework import viewsets

from ecomstore.apps.cart.mixins import ListCartMixin, CreateCartMixin


class ShowCartViewSet(ListCartMixin,
                      CreateCartMixin,
                      viewsets.ViewSet):
    # TODO - add permission classes
    pass
