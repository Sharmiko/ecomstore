from rest_framework.routers import DefaultRouter

from ecomstore.apps.checkout.views import CreditCartViewSet


router = DefaultRouter()
router.register(r'cc', CreditCartViewSet, r'cc')

urlpatterns = router.urls
