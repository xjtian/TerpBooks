from __future__ import absolute_import

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.test import TestCase
from django.test.client import Client


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
