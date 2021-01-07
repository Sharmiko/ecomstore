from rest_framework import viewsets

from ecomstore.apps.catalog.mixins import (
    ListCategoryMixin, RetrieveProductMixin
)


class CatalogViewSet(ListCategoryMixin,
                     RetrieveProductMixin,
                     viewsets.ViewSet):
    # TODO - add permission classes
    pass
