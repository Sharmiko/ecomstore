from rest_framework import viewsets

from ecomstore.apps.catalog.mixins import (
    ListCategoryMixin, RetrieveProductMixin
)


class CategoryViewSet(ListCategoryMixin,
                      viewsets.ViewSet):
    # TODO - add permission classes
    pass


class ProductViewSet(RetrieveProductMixin,
                     viewsets.ViewSet):
    # TODO - add permission classes
    pass
