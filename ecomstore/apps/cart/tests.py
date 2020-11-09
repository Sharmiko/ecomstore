import uuid

from django.test import TestCase

from rest_framework.test import APIClient

from ecomstore.apps.cart.models import CartItem
from ecomstore.apps.cart.utils import _generate_cart_id
from ecomstore.apps.catalog.models import Product


class CartTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
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

        Product(
            uuid=uuid.UUID('75616091-f312-442a-a8bd-b433a5003200'),
            name="Chemises de travail en coton à manches courtes",
            brand=None,
            sku='SKU893336',
            price=58.29,
            old_price=82.99,
            currency='USD',
            quantity=4,
            meta_keyword='men,Shirts,Bleu foncé'
        ).save()

        Product(
            uuid=uuid.UUID('7b88dc16-88a9-4446-a2d3-42907c815660'),
            name="Chemises imprimées ethniques pour hommes",
            brand=None,
            sku='SKUE92625',
            price=23.09,
            old_price=33.94,
            currency='USD',
            quantity=0,
            meta_keyword='men,Shirts,Blue'
        ).save()

    def test_add_cart_item(self):
        data = {
            'id': _generate_cart_id(),
            'quantity': 1,
            'product_uuid': '7b88dc16-88a9-4446-a2d3-42907c815660'
        }
        response = self.client.post('/api/show_cart/', data=data)
        self.assertEqual(response.status_code, 200)

        cart_id = CartItem.objects.first().cart_id

        data = {
            'id': cart_id,
            'quantity': 1,
            'product_uuid': '75616091-f312-442a-a8bd-b433a5003200'
        }
        response = self.client.post('/api/show_cart/', data=data)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/api/show_cart/?cart_id={cart_id}')
        self.assertEqual(len(response.data.get('cart')), 2)

