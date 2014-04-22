from __future__ import absolute_import

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django.test import TestCase

from books.models import Textbook
from ..models import Listing, TransactionRequestThread, TransactionRequest


class ListingTests(TestCase):
    def setUp(self):
        self.book, _ = Textbook.objects.get_or_create(title='title')
        self.user = User.objects.create_user(username='user', password='password')
        for listing in Listing.objects.all():
            listing.delete()

    def test_asking_price_validators(self):
        l = Listing(asking_price=0, book=self.book, owner=self.user)
        l.save()

        with self.assertRaises(ValidationError):
            l.delete()
            Listing(asking_price=-1, book=self.book, owner=self.user).save()

    def test_unicode(self):
        l, _ = Listing.objects.get_or_create(asking_price=1, book=self.book, owner=self.user)
        self.assertEqual(u'title: Available', unicode(l))

        l.status = Listing.PENDING
        l.save()

        self.assertEqual(u'title: Transaction Pending', unicode(l))

    def test_request_count(self):
        l, _ = Listing.objects.get_or_create(asking_price=1, book=self.book, owner=self.user)
        self.assertEqual(0, l.request_count())

        for i in xrange(0, 4):
            TransactionRequestThread.objects.create(listing=l, sender=self.user)

        self.assertEqual(4, l.request_count())

    def test_unread_messages(self):
        l, _ = Listing.objects.get_or_create(asking_price=1, book=self.book, owner=self.user)
        self.assertEqual(0, l.unread_messages())

        for i in xrange(0, 4):
            t = TransactionRequestThread.objects.create(listing=l, sender=self.user)
            for j in xrange(0, 3):
                TransactionRequest.objects.create(created_by=self.user, price=1, thread=t)

        self.assertEqual(12, l.unread_messages())

    def test_is_sold(self):
        l, _ = Listing.objects.get_or_create(asking_price=1, book=self.book, owner=self.user, status=Listing.SOLD)
        self.assertTrue(l.is_sold())

        l.status = Listing.AVAILABLE
        l.save()
        self.assertFalse(l.is_sold())

        l.status = Listing.PENDING
        l.save()
        self.assertFalse(l.is_sold())

    def test_is_available(self):
        l, _ = Listing.objects.get_or_create(asking_price=1, book=self.book, owner=self.user, status=Listing.AVAILABLE)
        self.assertTrue(l.is_available())

        l.status = Listing.SOLD
        l.save()
        self.assertFalse(l.is_available())

        l.status = Listing.PENDING
        l.save()
        self.assertFalse(l.is_available())

    def test_is_pending(self):
        l, _ = Listing.objects.get_or_create(asking_price=1, book=self.book, owner=self.user, status=Listing.PENDING)
        self.assertTrue(l.is_pending())

        l.status = Listing.SOLD
        l.save()
        self.assertFalse(l.is_pending())

        l.status = Listing.AVAILABLE
        l.save()
        self.assertFalse(l.is_pending())
