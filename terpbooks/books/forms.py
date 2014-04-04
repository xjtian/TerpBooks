from __future__ import absolute_import

from django import forms

from terpbooks.forms import BootstrapForm, BootstrapModelForm
from .models import Textbook, Semester, Professor, Author


class TextbookForm(BootstrapModelForm):
    class Meta:
        model = Textbook
        fields = ('title', 'edition', 'isbn', 'course_code', )


class SemesterForm(BootstrapModelForm):
    class Meta:
        model = Semester
        fields = ('semester', 'year', )


class NameSplitBootstrapForm(BootstrapForm):
    def __init__(self, model_class, *args, **kwargs):
        self.first_name_field = kwargs.pop('first_name_field', 'first_name')
        self.last_name_field = kwargs.pop('last_name_field', 'last_name')
        self.model_class = model_class

        self.name_field_name = kwargs.pop('name_field_name', 'name')

        super(NameSplitBootstrapForm, self).__init__(*args, **kwargs)

        self.fields[self.name_field_name] = forms.CharField(max_length=60)
        self.fields[self.name_field_name].widget.attrs.update({'class': 'form-control'})

    def is_valid(self):
        valid = super(NameSplitBootstrapForm, self).is_valid()
        if not valid:
            return False

        if len(self.cleaned_data['name_field_name']) == 0:
            return True

        first_name, last_name = self.cleaned_data[self.name_field_name].split()
        if len(first_name) == 0:
            self._errors['empty_fn'] = 'Empty first name'
            return False
        if len(last_name) == 0:
            self._errors['empty_ln'] = 'Empty Last name'
            return False

        return True

    def save(self, commit=True):
        if len(self.cleaned_data['name_field_name']) == 0:
            return None

        fn, ln = self.cleaned_data['professor'].split()
        if self.model_class.objects.filter(first_name=fn, last_name=ln).exists():
            return self.model_class.objects.get(first_name=fn, last_name=ln)

        p = self.model_class(**{self.first_name_field: fn, self.last_name_field: ln})
        if commit:
            p.save()

        return p


class AuthorForm(NameSplitBootstrapForm):
    def __init__(self, *args, **kwargs):
        kwargs.update({'name_field_name': 'author'})
        super(AuthorForm, self).__init__(Author, *args, **kwargs)
