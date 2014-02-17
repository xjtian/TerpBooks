from __future__ import absolute_import

from .models import Message, MessageThread

from rest_framework import serializers


class MessageThreadSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(required=True)
    recipient = serializers.PrimaryKeyRelatedField(required=True)

    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = MessageThread


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(required=True)
    thread = serializers.PrimaryKeyRelatedField(required=True)

    class Meta:
        model = Message
