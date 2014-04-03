from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import ListingListView, ListingDetailView


urlpatterns = patterns('',
    url(r'^listings/all$', ListingListView.as_view(), name='listings-all'),
    url(r'^listings/all/(?P<pk>\d+)$', ListingDetailView.as_view(), name='listings-detail-tmpl'),
)