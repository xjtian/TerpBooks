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
