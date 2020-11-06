from django.contrib import admin

from ecomstore.apps.cart.models import CartItem


class CartAdmin(admin.ModelAdmin):
    # set values for how it will be listed on admin
    list_display = ('cart_id', 'date_added', 'quantity', 'product', )
    list_display_links = ('cart_id',)
    list_per_page = 20
    ordering = ['date_added']
    search_fields = ['product',]


admin.site.register(CartItem, CartAdmin)

