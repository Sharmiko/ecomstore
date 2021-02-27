from typing import List

from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from ecomstore.apps.search.models import SearchTerm
from ecomstore.apps.catalog.models import Product
from ecomstore.apps.catalog.serializers import ProductSerializer


class SearchViewSet(viewsets.ViewSet):

    STRIP_WORDS = ['a', 'an', 'and', 'by', 'for', 'from', 'in', 'no', 'not',
                   'of', 'on', 'or', 'that', 'the', 'to', 'with']

    queryset = Product.objects.all()

    @action(detail=False, methods=['POST'])
    def search(self, request) -> Response:
        """ Get products matching the search text
        """
        search_text = request.data.get('q', str())
        page = int(request.data.get('page', 1))
        self.store(request, search_text)

        words = self.prepare_words(search_text)
        results = list()
        total = 0
        for word in words:
            products = self.queryset.filter(
                Q(name__icontains=word) |
                Q(sku__iexact=word) |
                Q(brand__icontains=word) |
                Q(meta_keyword__icontains=word)
            )
            total += products.count()
            results.append(products)

        res = list()
        for item in results:
            serializer = ProductSerializer(item, many=True)
            res.append(serializer.data)

        return Response(
            {
                'results': res,
                'total': total
            },
            status=status.HTTP_200_OK
        )

    @staticmethod
    def store(request, q: str) -> None:
        """ Store the search text in database
        """
        if len(q) > 2:
            term = SearchTerm()
            term.q = q

            x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded:
                ip = x_forwarded.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            term.ip_address = ip
            # TODO save user
            term.save()

    def prepare_words(self, search_text: str) -> List[str]:
        """ Remove common words and limit to 5 words
        """
        words = search_text.split()
        for common in self.STRIP_WORDS:
            if common in words:
                words.remove(common)

        return words[0:5]


