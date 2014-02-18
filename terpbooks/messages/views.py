from __future__ import absolute_import

from rest_framework import viewsets

from .models import Message, MessageThread
from .serializers import MessageSerializer, MessageThreadSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageThreadViewSet(viewsets.ModelViewSet):
    queryset = MessageThread.objects.all()
    serializer_class = MessageThreadSerializer