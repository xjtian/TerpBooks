from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'terpbooks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls')),
    url(r'^transactions/', include('transactions.urls')),
    url(r'^messages/', include('messages.urls')),
)

if settings.USE_CAS:
    urlpatterns += patterns('',
        url(r'^accounts/login$', 'cas.views.login', name='login'),
        url(r'^accounts/logout$', 'cas.views.logout', name='logout'),
    )
