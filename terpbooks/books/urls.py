from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import DynamicAuthorForms


urlpatterns = patterns('',
    url(r'^authorformset/$', DynamicAuthorForms.as_view(), name='author-formset'),
)
