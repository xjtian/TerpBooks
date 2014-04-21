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

        try:
            Semester(year=date.today().year + 1, semester=Semester.FALL).save()
            Semester(year=2005, semester=Semester.FALL).save()
        except ValidationError:
            self.fail('Semester model validator rejected valid fields.')


class ProfessorTests(TestCase):
    def setUp(self):
        Professor.objects.get_or_create(first_name='Bob', last_name='Bobby')

    def test_unique_together(self):
        """
        Test the unique_together constraint on first_name and last_name.
        """
        with self.assertRaises(ValidationError):
            Professor(first_name='Bob', last_name='Bobby').save()

        try:
            Professor(first_name='Bob', last_name='Notbobby').save()
            Professor(first_name='Notbob', last_name='Bobby').save()
        except ValidationError:
            self.fail('Professor model unique_together rejected valid combination.')


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

        try:
            Textbook(title='title', isbn='123').save()
            Textbook(title='title', isbn=' - - -').save()
            Textbook(title='title', isbn='       1').save()
        except ValidationError:
            self.fail('Textbook model isbn validator rejected valid field.')

    def test_course_code_validator(self):
        with self.assertRaises(ValidationError):
            Textbook(title='title', course_code='aaaa').save()

        with self.assertRaises(ValidationError):
            Textbook(title='title', course_code='ABCD12').save()

        with self.assertRaises(ValidationError):
            Textbook(title='title', course_code='ABC123').save()

        try:
            Textbook(title='title', course_code='ABCD123').save()
        except ValidationError:
            self.fail('Textbook model course code validator rejected valid field.')

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

        try:
            Author.objects.get_or_create(first_name='Dead', last_name='Beef', book=book2)
        except ValidationError:
            self.fail('Author model unique_together rejected valid combination.')
