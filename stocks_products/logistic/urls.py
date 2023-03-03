from rest_framework.routers import DefaultRouter

from .test import TestSomething
from .views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
urlpatterns = router.urls
