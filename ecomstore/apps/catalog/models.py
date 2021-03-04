from django.db import models
from django.contrib.auth.models import User


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(
            is_active=True
        )


class Category(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    object = models.Manager()
    active = ActiveCategoryManager()

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_queryset().filter(
            is_active=True)


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
                                    help_text='Comma-delimited set of SEO '
                                              'keywords for meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    objects = models.Manager()
    active = ActiveProductManager()

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

    def cross_sells(self):
        from ecomstore.apps.checkout.models import Order, OrderItem

        orders = Order.objects.filter(orderitem__product=self)
        order_items = OrderItem.objects.filter(
            order__in=orders
        ).exclude(product=self)
        products = Product.active.filter(orderitem__in=order_items).distinct()

        return products

    def cross_sells_user(self):
        from ecomstore.apps.checkout.models import Order, OrderItem
        from django.contrib.auth.models import User

        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter(
            order__user__in=users
        ).exclude(product=self)
        products = Product.active.filter(orderitem__in=items).distinct()

        return products

    def cross_sells_hybrid(self):
        from ecomstore.apps.checkout.models import Order, OrderItem
        from django.contrib.auth.models import User
        from django.db.models import Q

        orders = Order.objects.filter(orderitem__product=self)
        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter(
            Q(order__in=orders) |
            Q(order__user__in=users)
        ).exclude(product=self)
        products = Product.active.filter(orderitem__in=items).distinct()

        return products


class ActiveProductReviewManager(models.Manager):
    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(
            is_approved=True)


class ProductReview(models.Model):
    RATINGS = (
        (5, 5), (4, 4), (3, 3), (2, 2), (1, 1),
    )

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField()

    objects = models.Manager()
    approved = ActiveProductReviewManager()
