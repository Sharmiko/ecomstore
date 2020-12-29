from rest_framework import viewsets

from ecomstore.apps.catalog.mixins import (
    ListCategoryMixin, RetrieveProductMixin
)


class CategoryList(ListCategoryMixin,
                   viewsets.ViewSet):
    # TODO - add permission classes
    pass


class ProductDetail(RetrieveProductMixin,
                    viewsets.ViewSet):
    # TODO - add permission classes
    pass
