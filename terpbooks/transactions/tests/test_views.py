from __future__ import absolute_import

from datetime import date, timedelta

from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client, RequestFactory

from django.contrib.auth.models import User

from books.models import Textbook, Author, Semester, Professor
from books.forms import TextbookForm, AuthorFormSet, SemesterForm, ProfessorForm

from ..models import Listing
from ..forms import ListingForm

from ..views import ListingList, ListingDetail, CreateEditListing, ProfileListings, BoxBase, Inbox, Outbox
from ..views import RequestThreadDisplay, RequestThreadSubmit, RequestThreadDetail, CreateListingRequest
from ..views import ListingModificationBase, DeleteListing, MarkListingPending, MarkListingSold, MarkListingAvailable


class ListingListTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        self.book1, _ = Textbook.objects.get_or_create(title='ABC', isbn='12', course_code='ABCD101')
        self.book2, _ = Textbook.objects.get_or_create(title='DEF', isbn='34', course_code='EFGH201')
        self.book3, _ = Textbook.objects.get_or_create(title='ABCDEF', isbn='1234', course_code='IJKL301')

        self.book4, _ = Textbook.objects.get_or_create(title='GHI', isbn='56', course_code='MNOP401')
        self.book5, _ = Textbook.objects.get_or_create(title='JKL', isbn='78', course_code='QRST501')
        self.book6, _ = Textbook.objects.get_or_create(title='GHIJKL', isbn='5678', course_code='UVWX601')

        self.seller = User.objects.create_user(username='user1', password='password')
        self.buyer = User.objects.create_user(username='user2', password='password')

        self.listing1, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book1, asking_price=1, date_created=date.today() - timedelta(1))
        self.listing2, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book2, asking_price=2, date_created=date.today() - timedelta(2))
        self.listing3, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book3, asking_price=3, date_created=date.today() - timedelta(3))
        self.listing4, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book4, asking_price=4, date_created=date.today() - timedelta(4))
        self.listing5, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book5, asking_price=5, date_created=date.today() - timedelta(5))
        self.listing6, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book6, asking_price=6, date_created=date.today() - timedelta(6))

    def test_properties(self):
        v = ListingList()

        self.assertEqual(Listing, v.model)
        self.assertEqual(10, v.paginate_by)
        self.assertEqual('listings_list', v.context_object_name)
        self.assertEqual('buy/list-partial.html', v.template_name)

        self.assertEqual(list(Listing.objects.select_related().order_by('-date_created')), list(v.queryset))

    def test_get_queryset_order_by(self):
        """
        Test get_queryset() method when provided order_by GET parameter.
        """
        v = ListingList()

        # No parameters
        request = self.factory.get('')
        v.request = request

        expected = Listing.objects.select_related().order_by('-date_created')
        self.assertEqual(list(expected), list(v.get_queryset()))

        # Try all 4 valid order_by params
        request = self.factory.get('', {u'order_by': u'book__title'})
        v.request = request
        expected = Listing.objects.select_related().order_by('book__title')
        self.assertEqual(list(expected), list(v.get_queryset()))

        request = self.factory.get('', {u'order_by': u'asking_price'})
        v.request = request
        expected = Listing.objects.select_related().order_by('asking_price')
        self.assertEqual(list(expected), list(v.get_queryset()))

        request = self.factory.get('', {u'order_by': u'-asking_price'})
        v.request = request
        expected = Listing.objects.select_related().order_by('-asking_price')
        self.assertEqual(list(expected), list(v.get_queryset()))

        request = self.factory.get('', {u'order_by': u'date_created'})
        v.request = request
        expected = Listing.objects.select_related().order_by('date_created')
        self.assertEqual(list(expected), list(v.get_queryset()))

        # Verify order by date created on invalid order_by param
        request = self.factory.get('', {u'order_by': u'dead_beef'})
        v.request = request
        expected = Listing.objects.select_related().order_by('-date_created')
        self.assertEqual(list(expected), list(v.get_queryset()))

    def test_get_queryset_filter(self):
        """
        Test get_queryset() method when provided filtering GET parameters.
        """
        v = ListingList()

        # No parameters
        request = self.factory.get('')
        v.request = request
        expected = [self.listing1, self.listing2, self.listing3, self.listing4, self.listing5, self.listing6]
        self.assertEqual(expected, list(v.get_queryset()))

        # Title parameter
        request = self.factory.get('', {u'title': u'ABC'})
        v.request = request
        expected = [self.listing1, self.listing3]
        self.assertEqual(expected, list(v.get_queryset()))

        request = self.factory.get('', {u'title': [u'ABC', u'JKL']})
        v.request = request
        expected = [self.listing1, self.listing3, self.listing5, self.listing6]
        self.assertEqual(expected, list(v.get_queryset()))

        request = self.factory.get('', {u'title': u'ZZZ'})
        v.request = request
        expected = []
        self.assertEqual(expected, list(v.get_queryset()))

        # ISBN parameter
        request = self.factory.get('', {u'isbn': u'23'})
        v.request = request
        expected = [self.listing3]
        self.assertEqual(expected, list(v.get_queryset()))

        request = self.factory.get('', {u'isbn': [u'12', u'67']})
        v.request = request
        expected = [self.listing1, self.listing3, self.listing6]
        self.assertEqual(expected, list(v.get_queryset()))

        request = self.factory.get('', {u'isbn': u'22'})
        v.request = request
        expected = []
        self.assertEqual(expected, list(v.get_queryset()))

        # Course code parameter
        request = self.factory.get('', {u'course_code': u'L3'})
        v.request = request
        expected = [self.listing3]
        self.assertEqual(expected, list(v.get_queryset()))

        request = self.factory.get('', {u'course_code': [u'ABCD', u'501']})
        v.request = request
        expected = [self.listing1, self.listing5]
        self.assertEqual(expected, list(v.get_queryset()))

        # Combined parameters
        request = self.factory.get('', {
            u'title': [u'ABC', u'JKL'], # 1, 3, 5, 6
            u'isbn': u'12', # 1, 3
            u'course_code': [u'IJKL', u'101']   # 1, 3
        })
        v.request = request
        expected = [self.listing1, self.listing3]
        self.assertEqual(expected, list(v.get_queryset()))


class ListingDetailTests(TestCase):
    def setUp(self):
        self.book1, _ = Textbook.objects.get_or_create(title='ABC', isbn='12', course_code='ABCD101')
        self.book2, _ = Textbook.objects.get_or_create(title='DEF', isbn='34', course_code='EFGH201')
        self.book3, _ = Textbook.objects.get_or_create(title='ABCDEF', isbn='1234', course_code='IJKL301')

        self.book4, _ = Textbook.objects.get_or_create(title='GHI', isbn='56', course_code='MNOP401')
        self.book5, _ = Textbook.objects.get_or_create(title='JKL', isbn='78', course_code='QRST501')
        self.book6, _ = Textbook.objects.get_or_create(title='GHIJKL', isbn='5678', course_code='UVWX601')

        self.seller = User.objects.create_user(username='user1', password='password')
        self.buyer = User.objects.create_user(username='user2', password='password')

        self.listing1, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book1, asking_price=1, date_created=date.today() - timedelta(1), status=Listing.PENDING)
        self.listing2, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book2, asking_price=2, date_created=date.today() - timedelta(2), status=Listing.SOLD)
        self.listing3, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book3, asking_price=3, date_created=date.today() - timedelta(3))
        self.listing4, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book4, asking_price=4, date_created=date.today() - timedelta(4))
        self.listing5, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book5, asking_price=5, date_created=date.today() - timedelta(5))
        self.listing6, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book6, asking_price=6, date_created=date.today() - timedelta(6))

    def test_properties(self):
        v = ListingDetail()

        self.assertEqual(Listing, v.model)
        self.assertEqual([self.listing3, self.listing4, self.listing5, self.listing6], list(v.queryset))
        self.assertEqual('listing', v.context_object_name)
        self.assertEqual('buy/listing-detail.html', v.template_name)


class CreateEditListingTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        self.prof, _ = Professor.objects.get_or_create(first_name='John', last_name='Doe')
        self.sem, _ = Semester.objects.get_or_create(semester=Semester.FALL, year=2010)
        self.book, _ = Textbook.objects.get_or_create(title='ABC',
                                                      isbn='12',
                                                      course_code='ABCD101',
                                                      professor=self.prof,
                                                      semester=self.sem)

        self.author1, _ = Author.objects.get_or_create(first_name='Dead', last_name='Beef', book=self.book)
        self.author1, _ = Author.objects.get_or_create(first_name='Beef', last_name='Dead', book=self.book)

        self.seller = User.objects.create_user(username='user', password='password')
        self.listing, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book, asking_price=1)

    def test_properties(self):
        v = CreateEditListing()

        self.assertEqual('sell/index.html', v.template_name)
        self.assertEqual('sell', v.post_url)

    def test_unbound_get(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('listing-form'))

        form = response.context['book_form']
        self.assertEqual(TextbookForm, form.__class__)
        self.assertEqual({}, form.data)

        form = response.context['professor_form']
        self.assertEqual(ProfessorForm, form.__class__)
        self.assertEqual({}, form.data)

        form = response.context['semester_form']
        self.assertEqual(SemesterForm, form.__class__)
        self.assertEqual({}, form.data)

        form = response.context['author_formset']
        self.assertEqual(AuthorFormSet, form.__class__)
        self.assertEqual(1, form.total_form_count())
        self.assertEqual({}, form.data)

        self.assertEqual('sell', response.context['active'])
        self.assertEqual(reverse('listing-form'), response.context['action'])