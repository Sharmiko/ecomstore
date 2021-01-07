from uuid import UUID

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from ecomstore.apps.catalog.models import Category, Product
from ecomstore.apps.catalog.serializers import (
    CategorySerializer, ProductSerializer
)


class ListCategoryMixin(object):
    """ List all categories
    """

    @action(detail=False, methods=['GET'])
    def get_categories(self, request) -> Response:
        """ returns all unique categories
        """
        categories = Category.objects.distinct().only('name')
        serializer = CategorySerializer(categories, many=True)
        data = [value for row in serializer.data for value in row.values()]

        return Response(
            {
                'categories': data
            },
            status=status.HTTP_200_OK
        )


class RetrieveProductMixin(object):
    """ Get product details based on its uuid
    """

    @action(detail=False, methods=['POST'])
    def retrieve_product(self, request) -> Response:
        """ get product based on uuid
        """
        uuid = request.data.get('uuid')
        if not uuid:
            return Response(
                {
                    'message': 'Product UUID was not provided',
                    'status': 'error'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        product = Product.objects.filter(uuid=UUID(uuid)).first()
        if not product:
            return Response(
                {
                    'message': 'Product with provided UUID was not found',
                    'status': 'error'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(product)

        return Response(
            {
                'product': serializer.data
            },
            status=status.HTTP_200_OK
        )
