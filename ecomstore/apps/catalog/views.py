from rest_framework.views import APIView
from rest_framework.response import Response

from ecomstore.apps.catalog.models import Category
from ecomstore.apps.catalog.serializers import CategorySerializer


class CategoryList(APIView):
    """ List all categories
    """

    def get(self, request, format=None) -> Response:
        """ returns all unique categories
        """
        categories = Category.objects.distinct().only('name')
        serializer = CategorySerializer(categories, many=True)
        data = [value for row in serializer.data for value in row.values()]

        return Response({'categories': data})

