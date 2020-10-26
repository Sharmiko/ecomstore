import os
import random

import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.server.settings.local')

import django
django.setup()

from ecomstore.apps.catalog.models import Category, Product

DATA_ROOT = './data/'

def add_data_to_db():
    for file in os.listdir(DATA_ROOT):
        if file.endswith('csv'):
            data = pd.read_csv(DATA_ROOT + file)
            is_category = Category.objects.filter(
                name=file.split('.')[0]).first()
            if is_category:
                continue
            category = Category.objects.create(
                name=file.split('.')[0],
                is_active=True
            )
            for idx, row in data.iterrows():
                is_product = Product.objects.filter(name=row['name']).first()
                if is_product:
                    continue
                is_slug = Product.objects.filter(slug='-'.join(
                    row['name'].split(' '))).first()
                if is_slug:
                    continue
                product = Product.objects.create(
                    name=row['name'],
                    slug='-'.join(row['name'].split(' ')),
                    brand=row['brand'],
                    sku=row['model'],
                    price=row['current_price'],
                    old_price=row['raw_price'],
                    currency=row['currency'],
                    image=row['variation_0_image'],
                    thumbnail=row['variation_0_thumbnail'],
                    quantity=random.randrange(0, 10),
                    meta_keyword=','.join(
                        [
                            row['category'], row['subcategory'],
                            str(row['variation_0_color'])
                        ]
                    ),
                )
                product.categories.set([category])
                product.save()


if __name__ == '__main__':
    add_data_to_db()

