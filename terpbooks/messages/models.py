from django.db import models
from django.conf import settings


class MessageThread(models.Model):
    """
    Container for a message thread.
    """
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_conversations')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_conversations')


class Message(models.Model):
    """
    A message.
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages')

    subject = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)

    thread = models.ForeignKey(MessageThread, related_name='messages')
