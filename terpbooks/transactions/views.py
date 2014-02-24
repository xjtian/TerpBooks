from __future__ import absolute_import

from rest_framework import viewsets, generics

from .models import Listing, TransactionRequest, TransactionRequestThread
from .serializers import ListingSerializer, RequestSerializer, RequestThreadSerializer, ListingNestedSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class TransactionRequestViewSet(viewsets.ModelViewSet):
    queryset = TransactionRequest.objects.all()
    serializer_class = RequestSerializer


class RequestThreadViewSet(viewsets.ModelViewSet):
    queryset = TransactionRequestThread.objects.all()
    serializer_class = RequestThreadSerializer


class ListingNestedBookView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingNestedSerializer