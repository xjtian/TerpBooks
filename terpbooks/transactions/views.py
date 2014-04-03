from __future__ import absolute_import

from rest_framework import viewsets, generics

from django.db.models import Q
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from books.forms import TextbookForm, AuthorForm, SemesterForm, ProfessorForm

from .models import Listing, TransactionRequest, TransactionRequestThread
from .serializers import ListingSerializer, RequestSerializer, RequestThreadSerializer, ListingNestedSerializer
from .forms import ListingForm


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

        sort_field = None
        for key in self.request.GET:
            if key == u'order_by':
                if self.request.GET[key] in [u'book__title', u'-asking_price', u'asking_price', u'-date_created']:
                    sort_field = self.request.GET[key]

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

        qs = qs.filter(query)
        if sort_field is not None:
            qs = qs.order_by(sort_field)

        return qs


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


class SellPage(View):
    """
    Sell page view
    """
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'sell/index.html', {
            'active': 'sell',
            'book_form': TextbookForm(),
            'listing_form': ListingForm(),
        })

    @method_decorator(login_required)
    def post(self, request):
        book_form = TextbookForm(request.POST)
        listing_form = ListingForm(request.POST)

        biv = book_form.is_valid()
        liv = listing_form.is_valid()

        if biv and liv:
            book = book_form.save()
            listing = listing_form.save(commit=False)

            listing.book = book
            listing.owner = request.user

            listing.save()

            return render(request, 'sell/index.html', {
                'active': 'sell',
                'book_form': TextbookForm(),
                'listing_form': ListingForm(),
                'success_message': 'Listing successfully added!',
            })

        return render(request, 'sell/index.html', {
            'active': 'sell',
            'book_form': book_form,
            'listing_form': listing_form,
            'error_message': 'There were issues with your submission',
        })
