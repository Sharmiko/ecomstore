import uuid

from django.test import TestCase

from rest_framework.test import APIClient

from ecomstore.apps.catalog.models import Category, Product


class CatalogTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.categories = [
            'accessories', 'bags', 'beauty', 'house', 'jewelary',
            'kids', 'men', 'shoes', 'women'
        ]
        for cat in self.categories:
            Category(uuid=uuid.uuid4(), name=cat).save()

        Product(
            uuid=uuid.UUID('681c804f-d9a7-4dec-b97b-fc06fcc6a553'),
            name="Gilets chauds d'extérieur élégants de couleur unie",
            brand=None,
            sku='SKU788804',
            price=54.99,
            old_price=81.99,
            currency='USD',
            quantity=3,
            meta_keyword='men,Gilets,rouge'
        ).save()

    def test_category_list_view(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(sorted(response.data.get('categories')),
                         sorted(self.categories))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view(self):
        response = self.client.post('/api/product/', data={
            'uuid': '681c804f-d9a7-4dec-b97b-fc06fcc6a553'
        })
        data = response.data.get('product')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get('name'),
                         "Gilets chauds d'extérieur élégants de couleur unie")
        self.assertEqual(data.get('sku'), 'SKU788804')
        self.assertEqual(data.get('quantity'), 3)

        response = self.client.post('/api/product/', data={})
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/product/', data={
            'uuid': '181c804f-d9a7-4dec-b97b-fc06fcc6a553'
        })
        self.assertEqual(response.status_code, 404)

