from __future__ import absolute_import

from .models import Message, MessageThread

from django.contrib import admin


class MessageInline(admin.StackedInline):
    model = Message


class MessageAdmin(admin.ModelAdmin):
    pass


class ThreadAdmin(admin.ModelAdmin):
    inlines = [
        MessageInline,
    ]


admin.site.register(Message, MessageAdmin)
admin.site.register(MessageThread, ThreadAdmin)

