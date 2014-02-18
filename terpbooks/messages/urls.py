from __future__ import absolute_import

from rest_framework import routers

from .views import MessageViewSet, MessageThreadViewSet


router = routers.SimpleRouter()
router.register(r'messages', MessageViewSet, base_name='messages')
router.register(r'threads', MessageThreadViewSet, base_name='threads')

urlpatterns = router.urls