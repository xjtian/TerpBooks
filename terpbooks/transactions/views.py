from __future__ import absolute_import

from rest_framework import viewsets, generics

from django.views.generic import ListView
from django.shortcuts import render

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


class ListingListView(ListView):
    model = Listing
    queryset = Listing.objects.filter(status=Listing.AVAILABLE).order_by('-date_created')

    paginate_by = 10

    context_object_name = 'listings_list'
    template_name = 'buy/list-partial.html'


def buy_index(request):
    """
    Buy page view.
    """
    return render(request, 'buy/index.html', {
        'active': 'buy',
    })
