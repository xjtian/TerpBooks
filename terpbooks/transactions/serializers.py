from __future__ import absolute_import

from rest_framework import serializers

from .models import Listing, TransactionRequestThread, TransactionRequest


class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(required=True)
    book = serializers.PrimaryKeyRelatedField(required=True)

    requests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Listing


class RequestThreadSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(required=True)
    listing = serializers.PrimaryKeyRelatedField(required=True)

    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TransactionRequestThread


class RequestSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(required=True)
    thread = serializers.PrimaryKeyRelatedField(required=True)

    class Meta:
        model = TransactionRequest
