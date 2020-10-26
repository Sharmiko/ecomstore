from django import forms

from ecomstore.apps.catalog.models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'slug', 'brand', 'sku', 'price', 'old_price', 'currency',
            'image', 'thumbnail', 'is_active', 'is_bestseller', 'is_featured',
            'quantity', 'meta_keyword', 'categories'
        )

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']

