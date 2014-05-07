from __future__ import absolute_import

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.test import TestCase
from django.test.client import Client

from ..views import unread_messages
from books.models import Textbook
from transactions.models import TransactionRequestThread, TransactionRequest, Listing


class BuyPageTests(TestCase):
    def test_context(self):
        c = Client()

        response = c.get(reverse('buy'))
        self.assertEqual('buy', response.context['active'])


class ProfilePageTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='password')

    def test_context(self):
        c = Client()
        c.login(username='user', password='password')

        response = c.get(reverse('profile'))
        self.assertEqual('profile', response.context['active'])


class SplashPageTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='password')

    def test_redirect(self):
        c = Client()

        response = c.get(reverse('splash'))
        self.assertEqual(200, response.status_code)

        c.login(username='user', password='password')
        response = c.get(reverse('splash'))
        self.assertEqual('http://testserver' + reverse('profile'), response.url)


class UnreadMessagesTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

        self.book1, _ = Textbook.objects.get_or_create(title='title')
        self.listing1, _ = Listing.objects.get_or_create(owner=self.user1, book=self.book1, asking_price=1)
        self.thread1, _ = TransactionRequestThread.objects.get_or_create(sender=self.user2, listing=self.listing1)
        TransactionRequest.objects.get_or_create(price=1, created_by=self.user2, thread=self.thread1)

        self.book2, _ = Textbook.objects.get_or_create(title='title2')
        self.listing2, _ = Listing.objects.get_or_create(owner=self.user2, book=self.book2, asking_price=1)
        self.thread2, _ = TransactionRequestThread.objects.get_or_create(sender=self.user1, listing=self.listing2)
        TransactionRequest.objects.get_or_create(price=1, created_by=self.user1, thread=self.thread2)

    def test_function(self):
        self.assertEqual(1, unread_messages(self.user1))
        self.assertEqual(1, unread_messages(self.user2))
