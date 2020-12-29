from django.db import models


class Category(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2,
        blank=True, default=0.00)
    currency = models.CharField(max_length=16)
    image = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    meta_keyword = models.CharField(max_length=255,
        help_text='Comma-delimited set of SEO keywords for meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
