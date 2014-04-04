from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import AuthorFormSetView


urlpatterns = patterns('',
    url(r'^authorformset/$', AuthorFormSetView.as_view(), name='author-formset'),
)
