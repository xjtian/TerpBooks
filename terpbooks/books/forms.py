from __future__ import absolute_import

from datetime import date

from django import forms
from django.forms.util import ErrorList
from django.forms.formsets import formset_factory
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from terpbooks.forms import BootstrapForm, BootstrapModelForm
from .models import Textbook, Semester, Professor, Author


class TextbookForm(BootstrapModelForm):
    class Meta:
        model = Textbook
        fields = ('title', 'edition', 'isbn', 'course_code', )


class SemesterForm(BootstrapForm):
    CHOICES = list(Semester.SEMESTER_CHOICES)
    CHOICES.insert(0, ('', ''))

    semester = forms.ChoiceField(choices=CHOICES,
                                 required=False)
    year = forms.IntegerField(required=False,
                              validators=[
                                  MinValueValidator(2000),
                                  MaxValueValidator(date.today().year + 1)
                              ])

    def is_valid(self):
        """
        Extra condition on base is_valid that rejects if only one field
        out of semester and year is filled out. Valid if both fields
        are filled out or blank.
        """
        valid = super(SemesterForm, self).is_valid()
        if not valid:
            return False

        sem_empty = len(self.cleaned_data['semester']) == 0
        year_empty = self.cleaned_data['year'] is None

        if sem_empty ^ year_empty:
            errors = self._errors.setdefault('__all__', ErrorList())
            errors.append(u'Semester and year must be provided together, or not at all.')
            return False

        return True

    def save(self, commit=True):
        """
        Returns the Semester instance this form is bound to. If the fields
        are blank, returns None. commit=True saves instance, False
        returns the instance without saving.
        """
        semester = self.cleaned_data['semester']
        year = self.cleaned_data['year']

        if len(semester) == 0 and year is None:
            return None

        existing = Semester.objects.filter(semester=semester, year=year)
        if existing.exists():
            return existing[0]

        s = Semester(semester=semester, year=year)
        if commit:
            s.save()

        return s


class NameSplitBootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.first_name_field = kwargs.pop('first_name_field', 'first_name')
        self.last_name_field = kwargs.pop('last_name_field', 'last_name')

        self.name_field_name = kwargs.pop('name_field_name', 'name')

        super(NameSplitBootstrapForm, self).__init__(*args, **kwargs)

        self.fields[self.name_field_name] = forms.CharField(max_length=60,
                                                            required=False,
                                                            validators=[RegexValidator(
                                                                regex=r'^[^ ]+ [^ ]+( [^ ]+)*$',
                                                                message='Names must have at 2 separate words. This '
                                                                        'field can be left blank.'
                                                            )])
        self.fields[self.name_field_name].widget.attrs.update({'class': 'form-control'})

    def split_name_field(self):
        """
        Returns the split first and last names from field input.
        """
        if not hasattr(self, 'cleaned_data') or self.name_field_name not in self.cleaned_data or len(self.cleaned_data[self.name_field_name]) == 0:
            return '', ''

        split = self.cleaned_data[self.name_field_name].split()
        if len(split) > 2:
            split[1] = u' '.join(split[1:])
            split = split[:2]

        fn, ln = split
        return fn, ln


class AuthorForm(NameSplitBootstrapForm):
    def __init__(self, *args, **kwargs):
        kwargs.update({'name_field_name': 'author'})
        super(AuthorForm, self).__init__(*args, **kwargs)

    def save(self, book, commit=True):
        """
        Returns the Author instance associated with the provided Textbook.
        Returns None if the form was blank. If commit=True, the instance
        is saved to the DB, otherwise it's returned without being saved.

        If the instance already exists in the database, this will return
        the existing instance no matter what the value of commit is, to
        respect the unique_together constraint of the Author model.
        """
        fn, ln = super(AuthorForm, self).split_name_field()
        if len(fn) == 0 or len(ln) == 0:
            return None

        if book is None:
            raise Exception('Cannot save author form with empty book.')

        # Respect unique_together
        existing = Author.objects.filter(first_name=fn, last_name=ln, book=book)
        if existing.exists():
            return existing[0]

        author = Author(first_name=fn, last_name=ln, book=book)

        if commit:
            author.save()

        return author


AuthorFormSet = formset_factory(AuthorForm)


class ProfessorForm(NameSplitBootstrapForm):
    def __init__(self, *args, **kwargs):
        kwargs.update({'name_field_name': 'professor'})
        super(ProfessorForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        fn, ln = super(ProfessorForm, self).split_name_field()

        if len(fn) == 0 or len(ln) == 0:
            return None

        # Respect unique_together constraint
        existing = Professor.objects.filter(first_name=fn, last_name=ln)
        if existing.exists():
            return existing[0]

        p = Professor(first_name=fn, last_name=ln)
        if commit:
            p.save()

        return p
