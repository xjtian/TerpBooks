from __future__ import absolute_import

from django.test import TestCase

from django.contrib.auth.models import User

from ..models import Textbook, Listing, TransactionRequest, TransactionRequestThread
from ..forms import ListingForm, TransactionRequestForm


class ListingFormTests(TestCase):
    def setUp(self):
        self.book, _ = Textbook.objects.get_or_create(title='title')
        self.user = User.objects.create_user(username='user1', password='password')

    def test_constructor(self):
        """
        Check that bootstrap form styles are attached to form fields.
        """
        f = ListingForm()
        self.assertEqual('form-control', f.fields['comments'].widget.attrs['class'])
        self.assertEqual('form-control', f.fields['asking_price'].widget.attrs['class'])

    def test_save(self):
        data = {
            'asking_price': 1,
            'comments': 'abc',
        }

        f = ListingForm(data=data)

        with self.assertRaises(Exception):
            f.save(book=None, owner=None)

        with self.assertRaises(Exception):
            f.save(book=self.book, owner=None)

        with self.assertRaises(Exception):
            f.save(book=None, owner=self.user)

        obj = f.save(commit=False, book=self.book, owner=self.user)
        self.assertEqual(Listing(owner=self.user, book=self.book, **data), obj)
        # Assert not saved to DB
        self.assertFalse(Listing.objects.all().exists())

        obj = f.save(book=self.book, owner=self.user)
        self.assertEqual(self.book, obj.book)
        self.assertEqual(self.user, obj.owner)
        self.assertEqual(data['asking_price'], obj.asking_price)
        self.assertEqual(data['comments'], obj.comments)
        # Assert saved to DB
        self.assertEqual(1, Listing.objects.all().count())


class TransactionRequestFormTests(TestCase):
    def setUp(self):
        self.book, _ = Textbook.objects.get_or_create(title='title')
        self.seller = User.objects.create_user(username='user1', password='password')
        self.buyer = User.objects.create_user(username='user2', password='password')
        self.listing, _ = Listing.objects.get_or_create(owner=self.seller, book=self.book, asking_price=1)
        self.thread, _ = TransactionRequestThread.objects.get_or_create(listing=self.listing, sender=self.buyer)

    def test_constructor(self):
        """
        Check for bootstrap form styles and 5 rows on textbox.
        """
        f = TransactionRequestForm()
        self.assertEqual('form-control', f.fields['text'].widget.attrs['class'])
        self.assertEqual(5, f.fields['text'].widget.attrs['rows'])
        self.assertEqual('form-control', f.fields['price'].widget.attrs['class'])

    def test_is_valid(self):
        data = {
            'text': 'hello world',
            'price': 1,
        }

        f = TransactionRequestForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertTrue(f.is_valid(thread=self.thread))
        self.assertTrue(f.is_valid(user=self.seller))
        self.assertTrue(f.is_valid(thread=self.thread, user=self.buyer))
        self.assertFalse(f.is_valid(thread=self.thread, user=self.seller))

    def test_save(self):
        data = {
            'text': 'hello world',
            'price': 1,
        }

        f = TransactionRequestForm(data=data)
        with self.assertRaises(Exception):
            f.save()

        with self.assertRaises(Exception):
            f.save(thread=self.thread)

        with self.assertRaises(Exception):
            f.save(user=self.buyer)

        obj = f.save(commit=False, thread=self.thread, user=self.buyer)
        self.assertEqual(TransactionRequest(created_by=self.buyer, thread=self.thread, **data), obj)
        # Assert not saved to DB
        self.assertFalse(TransactionRequest.objects.all().exists())

        obj = f.save(thread=self.thread, user=self.buyer)
        self.assertEqual(self.thread, obj.thread)
        self.assertEqual(self.buyer, obj.created_by)
        self.assertEqual(data['text'], obj.text)
        self.assertEqual(data['price'], obj.price)
        # Assert saved to DB
        self.assertEqual(1, TransactionRequest.objects.all().count())
