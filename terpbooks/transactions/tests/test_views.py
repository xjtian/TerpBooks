from __future__ import absolute_import

from datetime import date, timedelta

from django.core.urlresolvers import reverse
from django.http import Http404

from django.test import TestCase
from django.test.client import Client, RequestFactory

from django.contrib.auth.models import User

from books.models import Textbook, Author, Semester, Professor
from books.forms import TextbookForm, AuthorFormSet, SemesterForm, ProfessorForm

from ..models import Listing, TransactionRequest, TransactionRequestThread
from ..forms import ListingForm, TransactionRequestForm

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
        self.author2, _ = Author.objects.get_or_create(first_name='Beef', last_name='Dead', book=self.book)

        self.seller = User.objects.create_user(username='user', password='password')
        self.listing, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book, asking_price=1)

        self.buyer = User.objects.create_user(username='user2', password='password')

        self.book_sold, _ = Textbook.objects.get_or_create(title='DEF')
        self.listing_sold, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book_sold, asking_price=1, status=Listing.SOLD)

        self.book_pending, _ = Textbook.objects.get_or_create(title='GHI')
        self.listing_pending, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book_pending, asking_price=1, status=Listing.PENDING)

        self.book2, _ = Textbook.objects.get_or_create(title='JKL')
        self.listing2, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book2, asking_price=1)

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

    def test_unbound_post(self):
        self.client.login(username='user', password='password')

        # Normal POST
        book_data = {
            'title': 'title',
            'edition': 1,
            'isbn': '123',
            'course_code': 'ABCD123',
        }

        data = {
            'asking_price': 1,
            'professor': 'dead beef',
            'semester': Semester.FALL,
            'year': 2010,
            'form-INITIAL_FORMS': 1,
            'form-TOTAL_FORMS': 1,
            'form-0-author': 'beef dead',
        }
        data.update(book_data)

        response = self.client.post(reverse('listing-form'), data)
        self.assertEqual(200, response.status_code)

        # Assert the correct objects were created
        book = Textbook.objects.get(**book_data)
        for k, v in book_data.items():
            self.assertEqual(v, getattr(book, k))

        self.assertEqual(1, book.authors.all().count())
        author = book.authors.all()[0]
        self.assertEqual('beef', author.first_name)
        self.assertEqual('dead', author.last_name)

        self.assertEqual('dead', book.professor.first_name)
        self.assertEqual('beef', book.professor.last_name)

        self.assertEqual(Semester.FALL, book.semester.semester)
        self.assertEqual(2010, book.semester.year)

        listing = Listing.objects.get(book=book)
        self.assertEqual(1, listing.asking_price)

        # Invalid POST
        data = {
            'title': 'not created',
            'form-INITIAL_FORMS': 1,
            'form-TOTAL_FORMS': 1,
        }

        response = self.client.post(reverse('listing-form'), data)
        self.assertEqual(200, response.status_code)

        self.assertFalse(Textbook.objects.filter(title='not created').exists())
        self.assertIn('error_message', response.context)

    def test_bound_get(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('listing-form-bound', kwargs={'pk': self.listing.pk}))

        self.assertEqual(200, response.status_code)

        # Assert forms bound with correct data
        form = response.context['book_form']
        for field in form.fields:
            self.assertEqual(getattr(self.book, field), form[field].value())

        form = response.context['professor_form']
        self.assertEqual('John Doe', form['professor'].value())

        form = response.context['semester_form']
        self.assertEqual(Semester.FALL, form['semester'].value())
        self.assertEqual(2010, form['year'].value())

        formset = response.context['author_formset']
        self.assertEqual(3, formset.total_form_count())
        self.assertEqual('Dead Beef', formset[0]['author'].value())
        self.assertEqual('Beef Dead', formset[1]['author'].value())
        self.assertIsNone(formset[2]['author'].value())

        self.assertEqual('sell', response.context['active'])
        self.assertEqual(reverse('listing-form-bound', kwargs={'pk': self.listing.pk}), response.context['action'])

        # Assert forms returned even if semester, professor, and author are blank
        response = self.client.get(reverse('listing-form-bound', kwargs={'pk': self.listing2.pk}))
        self.assertIsNone(response.context['semester_form']['semester'].value())
        self.assertIsNone(response.context['semester_form']['year'].value())

        self.assertIsNone(response.context['professor_form']['professor'].value())

        self.assertEqual(1, response.context['author_formset'].total_form_count())
        self.assertIsNone(response.context['author_formset'][0]['author'].value())

        # If listing not owned by user, reject
        self.client.logout()
        self.client.login(username='user2', password='password')
        response = self.client.get(reverse('listing-form-bound', kwargs={'pk': self.listing.pk}))

        self.assertEqual("You can't edit a listing you don't own!", response.context['error_message'])
        self.assertNotIn('book_form', response.context)
        self.assertNotIn('listing_form', response.context)
        self.assertNotIn('professor_form', response.context)
        self.assertNotIn('semester_form', response.context)
        self.assertNotIn('author_formset', response.context)

        # If listing pending or sold, reject
        self.client.logout()
        self.client.login(username='user', password='password')

        response = self.client.get(reverse('listing-form-bound', kwargs={'pk': self.listing_sold.pk}))
        self.assertEqual("You've marked this listing as sold, so it is uneditable.", response.context['error_message'])

        response = self.client.get(reverse('listing-form-bound', kwargs={'pk': self.listing_pending.pk}))
        self.assertEqual("You've marked this listing as pending, so it is uneditable.", response.context['error_message'])

    def test_bound_post(self):
        self.client.login(username='user', password='password')
        book_data = {
            'title': 'title changed',
            'edition': 1,
            'isbn': '123',
            'course_code': 'ABCD123',
        }

        data = {
            'asking_price': 11,
            'professor': 'chicken pork',
            'semester': Semester.SUMMER,
            'year': 2005,
            'form-INITIAL_FORMS': 3,
            'form-TOTAL_FORMS': 3,
            'form-0-author': 'pork chicken',
            'form-1-author': 'Dead Beef',
            'form-2-author': '',
        }
        data.update(book_data)

        response = self.client.post(reverse('listing-form-bound', kwargs={'pk': self.listing.pk}), data)
        self.assertEqual(200, response.status_code)

        def verify_data():
            book = Textbook.objects.get(pk=self.book.pk)
            for k, v in book_data.iteritems():
                self.assertEqual(v, getattr(book, k))

            self.assertEqual('chicken', book.professor.first_name)
            self.assertEqual('pork', book.professor.last_name)

            self.assertEqual(Semester.SUMMER, book.semester.semester)
            self.assertEqual(2005, book.semester.year)

            self.assertEqual(2, book.authors.count())
            self.assertEqual('Dead', book.authors.all()[0].first_name)
            self.assertEqual('Beef', book.authors.all()[0].last_name)

            self.assertEqual('pork', book.authors.all()[1].first_name)
            self.assertEqual('chicken', book.authors.all()[1].last_name)

            self.assertFalse(Author.objects.filter(first_name='Beef', last_name='Dead').exists())

            self.assertEqual(11, book.listing.asking_price)

        # Assert changes made
        verify_data()

        # If listing not owned by user, reject
        self.client.logout()
        self.client.login(username='user2', password='password')
        new_data = {
            'title': 'title changed AGAIN',
            'edition': 3,
            'isbn': '321',
            'course_code': 'DDDD123',
            'asking_price': 111,
            'professor': 'test test',
            'semester': Semester.SPRING,
            'year': 2004,
            'form-INITIAL_FORMS': 3,
            'form-TOTAL_FORMS': 3,
            'form-0-author': 'lllll lllll',
            'form-1-author': 'rrrrr rrrrr',
            'form-2-author': '',
        }
        response = self.client.post(reverse('listing-form-bound', kwargs={'pk': self.listing.pk}), new_data)

        self.assertEqual("You can't edit a listing you don't own!", response.context['error_message'])
        verify_data()

        # If listing pending or sold, reject
        self.client.logout()
        self.client.login(username='user', password='password')

        response = self.client.post(reverse('listing-form-bound', kwargs={'pk': self.listing_sold.pk}), new_data)
        self.assertEqual("You've marked this listing as sold, so it is uneditable.", response.context['error_message'])
        verify_data()

        response = self.client.post(reverse('listing-form-bound', kwargs={'pk': self.listing_pending.pk}), new_data)
        self.assertEqual("You've marked this listing as pending, so it is uneditable.", response.context['error_message'])
        verify_data()


class ProfileListingsTests(TestCase):
    def test_properties(self):
        v = ProfileListings()

        self.assertEqual(Listing, v.model)
        self.assertEqual('listings_list', v.context_object_name)
        self.assertEqual('profile/your-listings.html', v.template_name)

    def test_get_queryset(self):
        v = ProfileListings()

        user = User.objects.create_user(username='user', password='password')
        user2 = User.objects.create_user(username='user2', password='password')

        book1, _ = Textbook.objects.get_or_create(title='title1')
        book2, _ = Textbook.objects.get_or_create(title='title2')
        book3, _ = Textbook.objects.get_or_create(title='title3')

        yesterday = date.today() - timedelta(1)

        listing1, _ = Listing.objects.get_or_create(owner=user, book=book1, asking_price=1)
        listing2, _ = Listing.objects.get_or_create(owner=user, book=book2, asking_price=1, date_created=yesterday)
        listing3, _ = Listing.objects.get_or_create(owner=user2, book=book3, asking_price=1)

        factory = RequestFactory()
        request = factory.get('')

        request.user = user
        v.request = request
        self.assertEqual([listing1, listing2], list(v.get_queryset()))

        request.user = user2
        v.request = request
        self.assertEqual([listing3], list(v.get_queryset()))


class BoxBaseTests(TestCase):
    def test_properties(self):
        v = BoxBase()

        self.assertEqual(TransactionRequestThread, v.model)
        self.assertEqual('request_list', v.context_object_name)
        self.assertEqual('profile/inbox.html', v.template_name)
        self.assertIsNone(v.box)


class InboxTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

        self.book1, _ = Textbook.objects.get_or_create(title='title1')
        self.book2, _ = Textbook.objects.get_or_create(title='title2')

        self.listing1, _ = Listing.objects.get_or_create(owner=self.user1, book=self.book1, asking_price=1)
        self.listing2, _ = Listing.objects.get_or_create(owner=self.user2, book=self.book2, asking_price=1)

        self.thread1, _ = TransactionRequestThread.objects.get_or_create(sender=self.user2, listing=self.listing1)
        self.thread2, _ = TransactionRequestThread.objects.get_or_create(sender=self.user1, listing=self.listing2)

    def test_properties(self):
        v = Inbox()

        self.assertEqual('inbox', v.box)

    def test_get_context_data(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('inbox'))

        self.assertEqual('inbox', response.context['box'])

    def test_get_queryset(self):
        v = Inbox()

        request = self.factory.get('')
        request.user = self.user1
        v.request = request

        self.assertEqual([self.thread1], list(v.get_queryset()))

        request.user = self.user2
        self.assertEqual([self.thread2], list(v.get_queryset()))


class OutboxTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

        self.book1, _ = Textbook.objects.get_or_create(title='title1')
        self.book2, _ = Textbook.objects.get_or_create(title='title2')

        self.listing1, _ = Listing.objects.get_or_create(owner=self.user1, book=self.book1, asking_price=1)
        self.listing2, _ = Listing.objects.get_or_create(owner=self.user2, book=self.book2, asking_price=1)

        self.thread1, _ = TransactionRequestThread.objects.get_or_create(sender=self.user2, listing=self.listing1)
        self.thread2, _ = TransactionRequestThread.objects.get_or_create(sender=self.user1, listing=self.listing2)

    def test_properties(self):
        v = Outbox()

        self.assertEqual('outbox', v.box)

    def test_get_context_data(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('outbox'))

        self.assertEqual('outbox', response.context['box'])

    def test_get_queryset(self):
        v = Outbox()

        request = self.factory.get('')
        request.user = self.user1
        v.request = request

        self.assertEqual([self.thread2], list(v.get_queryset()))

        request.user = self.user2
        self.assertEqual([self.thread1], list(v.get_queryset()))


class RequestThreadDisplayTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

        self.book1, _ = Textbook.objects.get_or_create(title='title1')
        self.book2, _ = Textbook.objects.get_or_create(title='title2')

        self.listing1, _ = Listing.objects.get_or_create(owner=self.user1, book=self.book1, asking_price=1)
        self.listing2, _ = Listing.objects.get_or_create(owner=self.user2, book=self.book2, asking_price=1)

        self.thread1, _ = TransactionRequestThread.objects.get_or_create(sender=self.user2, listing=self.listing1)
        self.thread2, _ = TransactionRequestThread.objects.get_or_create(sender=self.user1, listing=self.listing2)

    def test_properties(self):
        v = RequestThreadDisplay()

        self.assertEqual(TransactionRequestThread, v.model)
        self.assertEqual('thread', v.context_object_name)
        self.assertEqual('profile/thread.html', v.template_name)

    def test_get_context_data(self):
        v = RequestThreadDisplay()

        request = self.factory.get('')
        request.user = self.user1
        v.request = request

        v.object = self.listing1
        context = v.get_context_data(pk=self.listing1.pk)

        form = context['form']
        self.assertEqual(TransactionRequestForm, form.__class__)

    def test_get_queryset(self):
        v = RequestThreadDisplay()

        request = self.factory.get('')

        request.user = self.user1
        v.request = request
        self.assertEqual([self.thread1, self.thread2], list(v.get_queryset()))

        request.user = self.user2
        v.request = request
        self.assertEqual([self.thread1, self.thread2], list(v.get_queryset()))

        request.user = User.objects.create_user(username='user3', password='password')
        v.request = request
        self.assertFalse(v.get_queryset().exists())


class RequestThreadSubmitTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

        self.book1, _ = Textbook.objects.get_or_create(title='title1')
        self.book2, _ = Textbook.objects.get_or_create(title='title2')

        self.listing1, _ = Listing.objects.get_or_create(owner=self.user1, book=self.book1, asking_price=1)
        self.listing2, _ = Listing.objects.get_or_create(owner=self.user2, book=self.book2, asking_price=1)

        self.thread1, _ = TransactionRequestThread.objects.get_or_create(sender=self.user2, listing=self.listing1)
        self.thread2, _ = TransactionRequestThread.objects.get_or_create(sender=self.user1, listing=self.listing2)

        self.user3 = User.objects.create_user(username='user3', password='password')
        self.unrelated_thread, _ = TransactionRequestThread.objects.get_or_create(sender=self.user3, listing=self.listing2)

    def test_properties(self):
        v = RequestThreadSubmit()

        self.assertEqual(TransactionRequestForm, v.form_class)
        self.assertEqual(TransactionRequestThread, v.model)
        self.assertEqual('thread', v.context_object_name)
        self.assertEqual('profile/thread.html', v.template_name)

    def test_get_success_url(self):
        v = RequestThreadSubmit()

        v.object = self.thread1
        self.assertEqual(reverse('thread', kwargs={'pk': self.thread1.pk}), v.get_success_url())

    def test_get_queryset(self):
        v = RequestThreadSubmit()
        request = self.factory.get('')
        request.user = self.user1

        v.request = request
        self.assertEqual([self.thread1, self.thread2], list(v.get_queryset()))

        request.user = self.user3
        self.assertEqual([self.unrelated_thread], list(v.get_queryset()))

    def test_form_valid(self):
        v = RequestThreadSubmit()
        request = self.factory.post('')
        request.user = self.user1
        v.request = request

        v.object = self.thread1

        form = TransactionRequestForm(data={'text': 'dead beef', 'price': 1})
        response = v.form_valid(form)

        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('thread', kwargs={'pk': self.thread1.pk}), response.url)
        # Assert message saved
        self.assertEqual(1, self.thread1.messages.count())

    def test_post(self):
        v = RequestThreadSubmit()
        request = self.factory.post('', {'text': 'dead beef', 'price': 1})
        request.user = self.user1

        v.request = request
        v.kwargs = {'pk': self.thread1.pk}

        response = v.post(request, **v.kwargs)
        self.assertEqual(302, response.status_code)
        # Assert message saved
        self.assertEqual(1, self.thread1.messages.count())
        self.assertEqual('dead beef', self.thread1.messages.all()[0].text)
        self.assertEqual(1, self.thread1.messages.all()[0].price)

        v.kwargs = {'pk': self.unrelated_thread.pk}
        # 404 - requested thread not in queryset (not allowed to access)
        with self.assertRaises(Http404):
            v.post(request, **v.kwargs)

        # 403 - listing not available (can't alter message history anymore)
        self.thread2.listing.status = Listing.PENDING
        self.thread2.listing.save()
        v.kwargs = {'pk': self.thread2.pk}
        response = v.post(request, **v.kwargs)
        self.assertEqual(403, response.status_code)

        self.thread2.listing.status = Listing.SOLD
        self.thread2.listing.save()
        response = v.post(request, **v.kwargs)
        self.assertEqual(403, response.status_code)
