from __future__ import absolute_import

from datetime import date

from django.test import TestCase

from ..models import Semester, Author, Professor
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
