from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic import RedirectView

from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .views import BuyPage, ProfilePage
from transactions.views import CreateEditListing

admin.autodiscover()

urlpatterns = patterns('')

if settings.USE_CAS:
    urlpatterns += patterns('',
        url(r'^accounts/login/$', 'cas.views.login', name='login'),
        url(r'^accounts/logout/$', 'cas.views.logout', name='logout'),
        url('^admin/logout/$', RedirectView.as_view(url=reverse_lazy('logout'))),
    )
else:
    urlpatterns += patterns('',
        url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
            'template_name': 'login.html',
        }, name='login'),

        url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {
            'template_name': 'logout.html',
        }, name='logout'),
    )

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls')),
    url(r'^transactions/', include('transactions.urls')),
    url(r'^buy$', BuyPage.as_view(), name='buy'),
    url(r'^sell$', login_required(CreateEditListing.as_view(template_name='sell/index.html', post_url='sell')), name='sell'),
    url(r'^profile$', login_required(ProfilePage.as_view()), name='profile'),
)
