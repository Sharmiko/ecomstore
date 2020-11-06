from rest_framework.routers import DefaultRouter

from ecomstore.apps.cart.views import ShowCartViewSet


router = DefaultRouter()
router.register(r'show_cart', ShowCartViewSet, r'show_cart')

urlpatterns = router.urls
print(urlpatterns)
