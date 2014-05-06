from __future__ import absolute_import

from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Semester, Professor, Textbook, Author


class SemesterTests(TestCase):
    def test_year_validator(self):
        """
        Test that the validator for the 'year' field rejects values less than
        2000 and greater than 1 beyond the current year, and accepts valid
        years.
        """
        with self.assertRaises(ValidationError):
            Semester(year=1999, semester=Semester.FALL).save()

        with self.assertRaises(ValidationError):
            Semester(year=date.today().year + 2, semester=Semester.FALL).save()

        Semester(year=date.today().year + 1, semester=Semester.FALL).save()
        Semester(year=2005, semester=Semester.FALL).save()

    def test_unicode(self):
        s, _ = Semester.objects.get_or_create(year=2010, semester=Semester.FALL)
        self.assertEqual(u'Fall 2010', unicode(s))


class ProfessorTests(TestCase):
    def setUp(self):
        Professor.objects.get_or_create(first_name='Bob', last_name='Bobby')

    def test_unique_together(self):
        """
        Test the unique_together constraint on first_name and last_name.
        """
        with self.assertRaises(ValidationError):
            Professor(first_name='Bob', last_name='Bobby').save()

        Professor(first_name='Bob', last_name='Notbobby').save()
        Professor(first_name='Notbob', last_name='Bobby').save()

    def test_unicode(self):
        p, _ = Professor.objects.get_or_create(first_name='Dead', last_name='Beef')
        self.assertEqual(u'Dead Beef', unicode(p))

        p, _ = Professor.objects.get_or_create(first_name='Dead', last_name='Beef Pork Chicken')
        self.assertEqual(u'Dead Beef Pork Chicken', unicode(p))


class TextbookTests(TestCase):
    def test_edition_validator(self):
        with self.assertRaises(ValidationError):
            Textbook(title='title', edition=0).save()

        try:
            Textbook(title='title', edition=1).save()
        except ValidationError:
            self.fail('Textbook model edition validator rejected valid field.')

    def test_isbn_validator(self):
        with self.assertRaises(ValidationError):
            Textbook(title='title', isbn='1234 -a').save()

        Textbook(title='title', isbn='123').save()
        Textbook(title='title', isbn=' - - -').save()
        Textbook(title='title', isbn='       1').save()

    def test_course_code_validator(self):
        with self.assertRaises(ValidationError):
            Textbook(title='title', course_code='aaaa').save()

        with self.assertRaises(ValidationError):
            Textbook(title='title', course_code='ABCD12').save()

        with self.assertRaises(ValidationError):
            Textbook(title='title', course_code='ABC123').save()

        Textbook(title='title', course_code='ABCD123').save()
        Textbook(title='title', course_code='ABCD123E').save()

    def test_authors_string(self):
        book, _ = Textbook.objects.get_or_create(title='title')
        self.assertEqual(u'Not provided', book.authors_string())

        Author.objects.get_or_create(first_name='Dead', last_name='Beef', book=book)
        self.assertEqual(u'Dead Beef', book.authors_string())

        Author.objects.get_or_create(first_name='Beef', last_name='Dead', book=book)
        self.assertEqual(u'Dead Beef, Beef Dead', book.authors_string())

        # Check that the author string is ordered alphabetically by last name
        Author.objects.get_or_create(first_name='FN', last_name='AAA', book=book)
        self.assertEqual(u'FN AAA, Dead Beef, Beef Dead', book.authors_string())

    def test_unicode(self):
        book, _ = Textbook.objects.get_or_create(title='title', isbn='123', course_code='ABCD123')
        self.assertEqual(u'title', unicode(book))


class AuthorTests(TestCase):
    def setUp(self):
        self.book, _ = Textbook.objects.get_or_create(title='title')

    def test_unique_together(self):
        """
        Test that unique_together rejects duplicate author names for the
        same book, but accepts the same name if assigned to a different
        book.
        """
        Author.objects.get_or_create(first_name='Dead', last_name='Beef', book=self.book)
        with self.assertRaises(ValidationError):
            Author(first_name='Dead', last_name='Beef', book=self.book).save()

        book2, _ = Textbook.objects.get_or_create(title='title2')

        Author.objects.get_or_create(first_name='Dead', last_name='Beef', book=book2)

    def test_unicode(self):
        a, _ = Author.objects.get_or_create(first_name='Dead', last_name='Beef', book=self.book)
        self.assertEqual(u'Dead Beef', unicode(a))

        a, _ = Author.objects.get_or_create(first_name='Dead', last_name='Beef Pork Chicken', book=self.book)
        self.assertEqual(u'Dead Beef Pork Chicken', unicode(a))
