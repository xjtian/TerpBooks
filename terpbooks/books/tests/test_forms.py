from __future__ import absolute_import

from datetime import date

from django import forms
from django.test import TestCase

from ..models import Semester, Author, Professor, Textbook
from ..forms import SemesterForm, NameSplitBootstrapForm, AuthorForm, ProfessorForm


class SemesterFormTests(TestCase):
    def test_year_validators(self):
        fall = SemesterForm.CHOICES[1][0]
        data = {'semester': fall}

        # Year in range
        data['year'] = 2010
        s = SemesterForm(data=data)
        self.assertTrue(s.is_valid())

        data['year'] = date.today().year + 1
        s = SemesterForm(data=data)
        self.assertTrue(s.is_valid())

        # Year too low
        data['year'] = 1999
        s = SemesterForm(data=data)
        self.assertFalse(s.is_valid())

        # Year too high
        data['year'] = date.today().year + 2
        s = SemesterForm(data=data)
        self.assertFalse(s.is_valid())

    def test_is_valid(self):
        # Empty cases
        s = SemesterForm(data={'semester': SemesterForm.CHOICES[0][0]})
        self.assertTrue(s.is_valid())

        s = SemesterForm(data={})
        self.assertTrue(s.is_valid())

        # Standard case - both filled out
        data = {'semester': SemesterForm.CHOICES[1][0], 'year': 2010}
        s = SemesterForm(data=data)
        self.assertTrue(s.is_valid())

        # Semester filled out, year empty
        data.pop('year')
        s = SemesterForm(data=data)
        self.assertFalse(s.is_valid())

        # Year filled out, semester empty
        data.pop('semester')
        data['year'] = 2010
        s = SemesterForm(data=data)
        self.assertFalse(s.is_valid())

        data['semester'] = SemesterForm.CHOICES[0][0]
        s = SemesterForm(data=data)
        self.assertFalse(s.is_valid())

    def test_save(self):
        # Empty cases
        s = SemesterForm(data={})
        self.assertTrue(s.is_valid())
        self.assertIsNone(s.save())
        self.assertIsNone(s.save(commit=False))

        data = {'semester': SemesterForm.CHOICES[0][0]}
        s = SemesterForm(data=data)
        self.assertTrue(s.is_valid())
        self.assertIsNone(s.save())
        self.assertIsNone(s.save(commit=False))

        # Standard cases
        data['year'] = 2010
        data['semester'] = SemesterForm.CHOICES[1][0]
        s = SemesterForm(data=data)
        self.assertTrue(s.is_valid())

        obj = s.save(commit=False)
        self.assertEqual(Semester(semester=Semester.FALL, year=2010), obj)
        # Verify not saved to DB
        self.assertFalse(Semester.objects.filter(semester=Semester.FALL, year=2010).exists())

        obj = s.save()
        self.assertEqual(Semester.FALL, obj.semester)
        self.assertEqual(2010, obj.year)
        # Verify saved to DB
        self.assertTrue(Semester.objects.filter(semester=Semester.FALL, year=2010).exists())


class NameSplitBootstrapFormTests(TestCase):
    def test_constructor(self):
        # Don't pass field names in constructor kwargs
        f = NameSplitBootstrapForm()

        self.assertEqual('first_name', f.first_name_field)
        self.assertEqual('last_name', f.last_name_field)
        self.assertEqual('name', f.name_field_name)

        # Did the field get instantiated? Is it a bootstrap control?
        self.assertEqual(forms.CharField, f.fields['name'].__class__)
        self.assertEqual('form-control', f.fields['name'].widget.attrs['class'])

        # Pass all field names
        f = NameSplitBootstrapForm(first_name_field='a', last_name_field='b', name_field_name='c')
        self.assertEqual('a', f.first_name_field)
        self.assertEqual('b', f.last_name_field)
        self.assertEqual('c', f.name_field_name)

        # Did the field get instantiated? Is it a bootstrap control?
        self.assertEqual(forms.CharField, f.fields['c'].__class__)
        self.assertEqual('form-control', f.fields['c'].widget.attrs['class'])

    def test_validators(self):
        # Empty valid
        data = {'name': ''}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())

        # Two words valid
        data = {'name': 'dead beef'}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())

        # More than two words valid
        data = {'name': 'dead beef pork chicken'}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())

        # Weird stuff valid
        data = {'name': '12.8x8d &#^$%$()v'}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())

        # One word not valid
        data = {'name': 'dead'}
        f = NameSplitBootstrapForm(data=data)
        self.assertFalse(f.is_valid())

        # One word with spaces after not valid
        data = {'name': 'dead   '}
        f = NameSplitBootstrapForm(data=data)
        self.assertFalse(f.is_valid())

    def test_save_helper(self):
        # No cleaned_data attribute (don't call is_valid)
        f = NameSplitBootstrapForm(data={})
        self.assertEqual(('', ''), f.split_name_field())

        # Invalid form
        data = {'name': 'dead'}
        f = NameSplitBootstrapForm(data=data)
        self.assertFalse(f.is_valid())
        self.assertEqual(('', ''), f.split_name_field())

        # Empty field
        data = {'name': ''}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(('', ''), f.split_name_field())

        # Two words
        data = {'name': 'dead beef'}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(('dead', 'beef'), f.split_name_field())

        # More than two words - first name first word, last name everything else
        data = {'name': 'dead beef pork chicken'}
        f = NameSplitBootstrapForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(('dead', 'beef pork chicken'), f.split_name_field())


class AuthorFormTests(TestCase):
    def test_constructor(self):
        f = AuthorForm()

        self.assertEqual('first_name', f.first_name_field)
        self.assertEqual('last_name', f.last_name_field)
        self.assertEqual('author', f.name_field_name)

        # Did the field get instantiated? Is it a bootstrap control?
        self.assertEqual(forms.CharField, f.fields['author'].__class__)
        self.assertEqual('form-control', f.fields['author'].widget.attrs['class'])

    def test_save(self):
        # Empty form returns None
        f = AuthorForm(data={'author': ''})
        self.assertIsNone(f.save(None))
        self.assertTrue(f.is_valid())
        self.assertIsNone(f.save(None))

        data = {'author': 'dead beef'}
        book, _ = Textbook.objects.get_or_create(title='title')

        # Standard case
        f = AuthorForm(data=data)
        self.assertTrue(f.is_valid())

        obj = f.save(book, commit=False)
        self.assertEqual(Author(first_name='dead', last_name='beef', book=book), obj)
        # Assert not saved to DB
        self.assertFalse(Author.objects.all().exists())

        obj = f.save(book)
        self.assertEqual('dead', obj.first_name)
        self.assertEqual('beef', obj.last_name)
        self.assertEqual(book, obj.book)
        # Assert saved to DB
        self.assertTrue(Author.objects.filter(first_name='dead', last_name='beef', book=book).exists())

        # Existing author object - test respect unique_together
        f = AuthorForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(obj, f.save(book))

        f = AuthorForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(obj, f.save(book, commit=False))


class ProfessorFormTests(TestCase):
    def test_constructor(self):
        f = ProfessorForm()

        self.assertEqual('first_name', f.first_name_field)
        self.assertEqual('last_name', f.last_name_field)
        self.assertEqual('professor', f.name_field_name)

        # Did the field get instantiated? Is it a bootstrap control?
        self.assertEqual(forms.CharField, f.fields['professor'].__class__)
        self.assertEqual('form-control', f.fields['professor'].widget.attrs['class'])

    def test_save(self):
        # Empty form returns None
        f = ProfessorForm(data={'professor': ''})
        self.assertIsNone(f.save())
        self.assertTrue(f.is_valid())
        self.assertIsNone(f.save())

        data = {'professor': 'dead beef'}

        # Standard case
        f = ProfessorForm(data=data)
        self.assertTrue(f.is_valid())

        obj = f.save(commit=False)
        self.assertEqual(Professor(first_name='dead', last_name='beef'), obj)
        # Assert not saved to DB
        self.assertFalse(Professor.objects.all().exists())

        obj = f.save()
        self.assertEqual('dead', obj.first_name)
        self.assertEqual('beef', obj.last_name)
        # Assert saved to DB
        self.assertTrue(Professor.objects.filter(first_name='dead', last_name='beef').exists())

        # Existing professor object - test respect unique_together
        f = ProfessorForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(obj, f.save())

        f = ProfessorForm(data=data)
        self.assertTrue(f.is_valid())
        self.assertEqual(obj, f.save(commit=False))
