from __future__ import absolute_import

from rest_framework import viewsets, generics

from django.db.models import Q
from django.views.generic import ListView, DetailView
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
    queryset = Listing.objects.select_related().filter(status=Listing.AVAILABLE).order_by('-date_created')

    paginate_by = 3

    context_object_name = 'listings_list'
    template_name = 'buy/list-partial.html'

    def get_queryset(self):
        qs = super(ListingListView, self).get_queryset()
        query = Q()

        for key in self.request.GET:
            if key not in [u'title', u'isbn', u'course_code']:
                continue

            iexact = 'book__%s__iexact' % key
            icontains = 'book__%s__icontains' % key
            values = self.request.GET.getlist(key)

            kquery = Q()
            for v in values:
                kquery |= Q(**{iexact: v})
                kquery |= Q(**{icontains: v})
            query &= kquery

        return qs.filter(query)


class ListingDetailView(DetailView):
    model = Listing
    queryset = Listing.objects.select_related().filter(status=Listing.AVAILABLE)

    context_object_name = 'listing'
    template_name = 'buy/listing-detail.html'


def buy_index(request):
    """
    Buy page view.
    """
    return render(request, 'buy/index.html', {
        'active': 'buy',
    })
