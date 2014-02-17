from __future__ import absolute_import

from .models import Listing, TransactionRequest, TransactionRequestThread

from django.contrib import admin


class ListingAdmin(admin.ModelAdmin):
    pass


class RequestInline(admin.StackedInline):
    model = TransactionRequest


class RequestAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    inlines = [
        RequestInline,
    ]


admin.site.register(Listing, ListingAdmin)
admin.site.register(TransactionRequest, RequestAdmin)
admin.site.register(TransactionRequestThread, ThreadAdmin)
