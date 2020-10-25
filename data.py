import os
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
            for row, idx in data.iterrows():
                # TODO - add data to models
                print(row)
                print(idx)
                break
            break


if __name__ == '__main__':
    add_data_to_db()

