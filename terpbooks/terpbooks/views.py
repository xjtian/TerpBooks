from django.views import generic
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from books.forms import TextbookForm, AuthorFormSet, ProfessorForm, SemesterForm
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
            'author_formset': AuthorFormSet(),
            'professor_form': ProfessorForm(),
            'semester_form': SemesterForm(),
        })

    @method_decorator(login_required)
    def post(self, request):
        book_form = TextbookForm(request.POST)
        listing_form = ListingForm(request.POST)
        author_formset = AuthorFormSet(request.POST)
        prof_form = ProfessorForm(request.POST)
        sem_form = SemesterForm(request.POST)

        biv = book_form.is_valid()
        liv = listing_form.is_valid()
        aiv = author_formset.is_valid()
        piv = prof_form.is_valid()
        siv = sem_form.is_valid()

        if biv and liv and aiv and piv and siv:
            book = book_form.save(commit=False)

            semester = sem_form.save(commit=True)
            if semester is not None:
                book.semester = semester

            prof = prof_form.save(commit=True)
            if prof is not None:
                book.professor = prof

            book.save()

            for form in author_formset.forms:
                author = form.save(commit=False)
                if author is not None:
                    author.book = book
                    author.save()

            listing = listing_form.save(commit=False)
            listing.book = book
            listing.owner = request.user
            listing.save()

            return render(request, 'sell/index.html', {
                'active': 'sell',
                'book_form': TextbookForm(),
                'listing_form': ListingForm(),
                'author_formset': AuthorFormSet(),
                'professor_form': ProfessorForm(),
                'semester_form': SemesterForm(),
                'success_message': 'Listing successfully added!',
            })

        return render(request, 'sell/index.html', {
            'active': 'sell',
            'book_form': book_form,
            'listing_form': listing_form,
            'author_formset': author_formset,
            'professor_form': prof_form,
            'semester_form': sem_form,
            'error_message': 'There were issues with your submission',
        })


class ProfilePage(generic.View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'profile/index.html', {
            'active': 'profile',
        })