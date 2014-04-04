from __future__ import absolute_import

from django import forms
from django.forms.util import ErrorList
from django.forms.formsets import formset_factory

from terpbooks.forms import BootstrapModelForm
from .models import Textbook, Semester, Professor, Author


class TextbookForm(BootstrapModelForm):
    class Meta:
        model = Textbook
        fields = ('title', 'edition', 'isbn', 'course_code', )


class SemesterForm(BootstrapModelForm):
    class Meta:
        model = Semester
        fields = ('semester', 'year', )


class NameSplitBootstrapForm(forms.Form):
    def __init__(self, model_class, *args, **kwargs):
        self.first_name_field = kwargs.pop('first_name_field', 'first_name')
        self.last_name_field = kwargs.pop('last_name_field', 'last_name')
        self.model_class = model_class

        self.name_field_name = kwargs.pop('name_field_name', 'name')

        super(NameSplitBootstrapForm, self).__init__(*args, **kwargs)

        self.fields[self.name_field_name] = forms.CharField(max_length=60, required=False)
        self.fields[self.name_field_name].widget.attrs.update({'class': 'form-control'})

    def is_valid(self):
        valid = super(NameSplitBootstrapForm, self).is_valid()
        if not valid:
            return False

        if self.name_field_name not in self.cleaned_data or len(self.cleaned_data[self.name_field_name]) == 0:
            return True

        split = self.cleaned_data[self.name_field_name].split()
        if len(split) < 2:
            errors = self._errors.setdefault(self.name_field_name, ErrorList())
            errors.append(u'Names must have at 2 separate words. This field can be left blank.')
            return False

        if len(split) > 2:
            split[1] = u' '.join(split[1:])
            split = split[:2]

        first_name, last_name = split
        if len(first_name) == 0:
            errors = self._errors.setdefault(self.name_field_name, ErrorList())
            errors.append(u'Empty first name')
            return False
        if len(last_name) == 0:
            errors = self._errors.setdefault(self.name_field_name, ErrorList())
            errors.append(u'Empty last name')
            return False

        return True

    def save(self, commit=True):
        if self.name_field_name not in self.cleaned_data or len(self.cleaned_data[self.name_field_name]) == 0:
            return None

        fn, ln = self.cleaned_data[self.name_field_name].split()
        if self.model_class.objects.filter(**{
            self.first_name_field: fn, self.last_name_field: ln
        }).exists():
            return self.model_class.objects.get(**{self.first_name_field: fn, self.last_name_field: ln})

        p = self.model_class(**{self.first_name_field: fn, self.last_name_field: ln})
        if commit:
            p.save()

        return p


class AuthorForm(NameSplitBootstrapForm):
    def __init__(self, *args, **kwargs):
        kwargs.update({'name_field_name': 'author'})
        super(AuthorForm, self).__init__(Author, *args, **kwargs)


AuthorFormSet = formset_factory(AuthorForm)


class ProfessorForm(NameSplitBootstrapForm):
    def __init__(self, *args, **kwargs):
        kwargs.update({'name_field_name': 'professor'})
        super(ProfessorForm, self).__init__(Professor, *args, **kwargs)
