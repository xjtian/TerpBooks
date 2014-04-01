from __future__ import absolute_import

from django.conf.urls import patterns, url

from rest_framework import routers

from .views import ListingViewSet, TransactionRequestViewSet, RequestThreadViewSet, ListingNestedBookView
from .views import ListingListView, ListingDetailView


router = routers.SimpleRouter()
router.register(r'listings', ListingViewSet, base_name='listings')
router.register(r'threads', RequestThreadViewSet, base_name='threads')
router.register(r'requests', TransactionRequestViewSet, base_name='requests')

urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^listings/all$', ListingListView.as_view(), name='listings-all'),
    url(r'^listings/all/(?P<pk>\d+)$', ListingDetailView.as_view(), name='listings-detail-tmpl'),
)