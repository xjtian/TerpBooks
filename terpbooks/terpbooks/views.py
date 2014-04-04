from django.views import generic
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from books.forms import TextbookForm
from transactions.forms import ListingForm


class BuyPage(generic.View):
    """
    Buy page view.
    """
    def get(self, request):
        return render(request, 'buy/index.html', {
            'active': 'buy',
        })


class SellPage(generic.View):
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