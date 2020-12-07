from rest_framework.routers import DefaultRouter

from ecomstore.apps.catalog.views import CategoryList, ProductDetail


router = DefaultRouter()
router.register(r'categories', CategoryList, r'categories')
router.register(r'product', ProductDetail, r'product')

urlpatterns = router.urls

