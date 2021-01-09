from rest_framework.routers import DefaultRouter

from ecomstore.apps.catalog.views import CategoryViewSet, ProductViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, r'categories')
router.register(r'product', ProductViewSet, r'product')

urlpatterns = router.urls
