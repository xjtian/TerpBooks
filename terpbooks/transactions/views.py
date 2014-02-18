from __future__ import absolute_import

from rest_framework import viewsets

from .models import Listing, TransactionRequest, TransactionRequestThread
from .serializers import ListingSerializer, RequestSerializer, RequestThreadSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class TransactionRequestViewSet(viewsets.ModelViewSet):
    queryset = TransactionRequest.objects.all()
    serializer_class = RequestSerializer


class RequestThreadViewSet(viewsets.ModelViewSet):
    queryset = TransactionRequestThread.objects.all()
    serializer_class = RequestThreadSerializer