from __future__ import absolute_import

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import ListingListView, ListingDetailView, YourListingsView


urlpatterns = patterns('',
    url(r'^listings/all$', ListingListView.as_view(), name='listings-all'),
    url(r'^listings/all/(?P<pk>\d+)$', ListingDetailView.as_view(), name='listings-detail-tmpl'),
    url(r'^listings/profile$', login_required(YourListingsView.as_view()), name='profile-listings')
)