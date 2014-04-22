from __future__ import absolute_import

from datetime import datetime, timedelta, tzinfo

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django.test import TestCase

from books.models import Textbook
from ..models import Listing, TransactionRequestThread, TransactionRequest


ZERO = timedelta(0)


class UTC(tzinfo):
    """UTC timezone class from python datetime module docs."""

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


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


class TransactionRequestThreadTests(TestCase):
    def setUp(self):
        self.book, _ = Textbook.objects.get_or_create(title='title')
        self.seller = User.objects.create_user(username='user', password='password')
        self.buyer = User.objects.create_user(username='user2', password='password')
        self.listing, _ = Listing.objects.get_or_create(asking_price=0, book=self.book, owner=self.seller)
        self.thread, _ = TransactionRequestThread.objects.get_or_create(listing=self.listing, sender=self.buyer)

        for r in TransactionRequest.objects.all():
            r.delete()

    def test_unread_messages_seller(self):
        self.assertEqual(0, self.thread.unread_messages_seller())
        for i in xrange(0, 5):
            TransactionRequest.objects.create(thread=self.thread, created_by=self.buyer, price=1)
            self.assertEqual(i + 1, self.thread.unread_messages_seller())

        for r in TransactionRequest.objects.all():
            r.read = True
            r.save()

        self.assertEqual(0, self.thread.unread_messages_seller())

    def test_unread_messages_buyer(self):
        self.assertEqual(0, self.thread.unread_messages_buyer())
        for i in xrange(0, 5):
            TransactionRequest.objects.create(thread=self.thread, created_by=self.seller, price=1)
            self.assertEqual(i + 1, self.thread.unread_messages_buyer())

        for r in TransactionRequest.objects.all():
            r.read = True
            r.save()

        self.assertEqual(0, self.thread.unread_messages_buyer())

    def test_last_buyer_offer_price(self):
        self.assertEqual(0, self.thread.last_buyer_offer_price())
        for i in xrange(0, 5):
            t = TransactionRequest.objects.create(thread=self.thread, created_by=self.buyer, price=i)
            t.date_created = datetime.now(tz=UTC()) + timedelta(i)
            t.save()

            self.assertEqual(i, self.thread.last_buyer_offer_price())

    def test_last_buyer_offer_time(self):
        self.assertEqual(None, self.thread.last_buyer_offer_time())
        for i in xrange(0, 5):
            t = TransactionRequest.objects.create(thread=self.thread, created_by=self.buyer, price=i)
            d = datetime.now(tz=UTC()) + timedelta(i)
            t.date_created = d
            t.save()

            self.assertEqual(d, self.thread.last_buyer_offer_time())

    def test_last_seller_offer_price(self):
        self.assertEqual(0, self.thread.last_seller_offer_price())
        for i in xrange(0, 5):
            t = TransactionRequest.objects.create(thread=self.thread, created_by=self.seller, price=i)
            t.date_created = datetime.now(tz=UTC()) + timedelta(i)
            t.save()

            self.assertEqual(i, self.thread.last_seller_offer_price())

    def last_seller_offer_time(self):
        self.assertEqual(None, self.thread.last_seller_offer_time())
        for i in xrange(0, 5):
            t = TransactionRequest.objects.create(thread=self.thread, created_by=self.seller, price=i)
            d = datetime.now(tz=UTC()) + timedelta(i)
            t.date_created = d
            t.save()

            self.assertEqual(d, self.thread.last_seller_offer_time())

    def test_last_message_time(self):
        self.assertEqual(None, self.thread.last_message_time())
        for i in xrange(0, 5):
            t = TransactionRequest.objects.create(thread=self.thread, created_by=self.seller, price=i)
            d = datetime.now(tz=UTC()) + timedelta(i)
            t.date_created = d
            t.save()

            self.assertEqual(d, self.thread.last_message_time())

    def test_chron_messages(self):
        self.assertFalse(self.thread.chron_messages().exists())

        tr = [None] * 5
        for i in xrange(0, 5):
            created = [self.seller, self.buyer][i % 2]
            t = TransactionRequest.objects.create(thread=self.thread, created_by=created, price=i)
            d = datetime.now(tz=UTC()) + timedelta(i)
            t.date_created = d
            t.save()

            tr[i] = t

        self.assertListEqual(list(self.thread.chron_messages()), tr)

    def test_mark_seen_by(self):
        self.thread.mark_seen_by(self.seller)
        self.assertEqual(0, len(TransactionRequest.objects.all()))
        self.thread.mark_seen_by(self.buyer)
        self.assertEqual(0, len(TransactionRequest.objects.all()))

        # Create messages
        for i in xrange(0, 5):
            TransactionRequest.objects.create(thread=self.thread, created_by=self.buyer, price=i)
            TransactionRequest.objects.create(thread=self.thread, created_by=self.seller, price=i)

        qs = self.thread.messages.all()
        for r in qs:
            self.assertFalse(r.read)

        self.thread.mark_seen_by(self.seller)
        # Assert buyer messages read
        qs = self.thread.messages.filter(created_by=self.buyer)
        for r in qs:
            self.assertTrue(r.read)
            r.read = False
            r.save()
        # Assert seller messages still unread
        qs = self.thread.messages.filter(created_by=self.seller)
        for r in qs:
            self.assertFalse(r.read)

        self.thread.mark_seen_by(self.buyer)
        # Assert seller messages read
        qs = self.thread.messages.filter(created_by=self.seller)
        for r in qs:
            self.assertTrue(r.read)
            r.read = False
            r.save()
        # Assert buyer messages still unread
        qs = self.thread.messages.filter(created_by=self.buyer)
        for r in qs:
            self.assertFalse(r.read)

        # If non-buyer and non-seller user passed, no change
        user = User.objects.create_user(username='user3', password='password')
        self.thread.mark_seen_by(user)
        for r in self.thread.messages.all():
            self.assertFalse(r.read)
