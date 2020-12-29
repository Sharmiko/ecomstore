from django.contrib import admin

from ecomstore.apps.catalog.models import Product, Category
from ecomstore.apps.catalog.forms import ProductAdminForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    # set values for how it will be listed on admin
    list_display = (
        'name', 'quantity', 'price', 'old_price', 'created_at',
        'updated_at'
    )
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = [
        'name', 'description', 'meta_keywords', 'meta_description'
    ]
    exclude = ('created_at', 'updated_at',)


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    # set values for how it will be listed on admin
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = [
        'name', 'description', 'meta_keywords', 'meta_description'
    ]
    exclude = ('created_at', 'updated_at',)


admin.site.register(Category, CategoryAdmin)
