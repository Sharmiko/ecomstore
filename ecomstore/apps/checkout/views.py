from rest_framework import viewsets

from ecomstore.apps.checkout.mixins import CreditCartMixin


class CreditCartViewSet(CreditCartMixin,
                        viewsets.ViewSet):
    # TODO - add permission classes
    pass
