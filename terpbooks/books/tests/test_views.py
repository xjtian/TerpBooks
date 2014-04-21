from __future__ import absolute_import

from django.core.urlresolvers import reverse
from django.forms.formsets import formset_factory

from django.test import TestCase
from django.test.client import Client

from ..forms import AuthorForm
from ..views import DynamicAuthorForms


class DynamicAuthorFormsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.view = DynamicAuthorForms()

        # Formset class for AuthorForm with no extras
        self.fs_class = formset_factory(AuthorForm, extra=0)

    def formset_to_dict(self, fs):
        """
        Turn a bound/unbound formset to a dictionary to POST.
        """
        data = {}
        for field in fs.management_form:
            data['form-%s' % field.name] = field.value()

        for i, form in enumerate(fs):
            for field in form:
                if field.value() is not None:
                    data['form-%d-%s' % (i, field.name)] = field.value()
                else:
                    data['form-%d-%s' % (i, field.name)] = ''

        return data

    def test_blank(self):
        """
        Test that on post of a blank formset, the view returns an
        unbound formset with one extra blank form.
        """
        # Post nothing
        a = self.fs_class(initial=[{'author': ''}])
        data = self.formset_to_dict(a)

        response = self.client.post(reverse('author-formset'), data)

        self.assertEqual(200, response.status_code)
        formset = response.context['author_formset']

        self.assertEqual(2, formset.total_form_count())
        for form in formset:
            self.assertEqual({}, form.data)

    def test_bound(self):
        """
        Test that on post of a formset with initial data, the view returns
        a bound formset with one extra blank form, and the previous
        forms with unchanged data.
        """
        a = self.fs_class(initial=[
            {'author': 'dead beef'},
            {'author': None},
            {'author': 'beef dead'},
        ])
        data = self.formset_to_dict(a)

        response = self.client.post(reverse('author-formset'), data)

        self.assertEqual(200, response.status_code)
        formset = response.context['author_formset']

        self.assertEqual(4, formset.total_form_count())
        self.assertEqual('dead beef', formset[0]['author'].value())
        self.assertEqual('', formset[1]['author'].value())
        self.assertEqual('beef dead', formset[2]['author'].value())
        self.assertIsNone(formset[3]['author'].value())
