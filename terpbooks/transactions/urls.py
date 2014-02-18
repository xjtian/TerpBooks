from __future__ import absolute_import

from rest_framework import routers

from .views import ListingViewSet, TransactionRequestViewSet, RequestThreadViewSet


router = routers.SimpleRouter()
router.register(r'listings', ListingViewSet, base_name='listings')
router.register(r'threads', RequestThreadViewSet, base_name='threads')
router.register(r'requests', TransactionRequestViewSet, base_name='requests')

urlpatterns = router.urls