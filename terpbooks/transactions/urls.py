from __future__ import absolute_import

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import ListingList, ListingDetail, ProfileListings, CreateEditListing, Inbox, Outbox, RequestThreadDetail, CreateListingRequest
from .views import DeleteListing, MarkListingPending, MarkListingSold, MarkListingAvailable


urlpatterns = patterns('',
    url(r'^listings/all$', ListingList.as_view(), name='listings-all'),
    url(r'^listings/all/(?P<pk>\d+)$', ListingDetail.as_view(), name='listings-detail-tmpl'),

    url(r'^listings/profile$', login_required(ProfileListings.as_view()), name='profile-listings'),

    url(r'^sell-form$',
        login_required(CreateEditListing.as_view(template_name='sell/sell_form.html',
                                post_url='listing-form')),
        name='listing-form'),
    url(r'^sell-form/(?P<pk>\d+)$',
        login_required(CreateEditListing.as_view(template_name='sell/sell_form.html',
                                post_url='listing-form-bound')),
        name='listing-form-bound'),

    url(r'^inbox$', login_required(Inbox.as_view()), name='inbox'),
    url(r'^outbox$', login_required(Outbox.as_view()), name='outbox'),

    url(r'^threads/(?P<pk>\d+)$', login_required(RequestThreadDetail.as_view()), name='thread'),
    url(r'^create-thread/(?P<pk>\d+)$', login_required(CreateListingRequest.as_view()), name='create_thread'),

    url(r'^delete-listing/(?P<pk>\d+)$', login_required(DeleteListing.as_view()), name='delete_listing'),
    url(r'^pending-listing/(?P<pk>\d+)$', login_required(MarkListingPending.as_view()), name='pending_listing'),
    url(r'^sold-listing/(?P<pk>\d+)$', login_required(MarkListingSold.as_view()), name='sold_listing'),
    url(r'^available-listing/(?P<pk>\d+)$', login_required(MarkListingAvailable.as_view()), name='available_listing'),
)