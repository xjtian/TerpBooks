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


class AuthorForm(BootstrapModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', )


class ProfessorForm(BootstrapForm):
    professor = forms.CharField(max_length=60)

    def is_valid(self):
        valid = super(ProfessorForm, self).is_valid()
        if not valid:
            return False

        first_name, last_name = self.cleaned_data['professor'].split()
        if len(first_name) == 0:
            self._errors['empty_fn'] = 'Empty first name'
            return False
        if len(last_name) == 0:
            self._errors['empty_ln'] = 'Empty Last name'
            return False

        return True

    def save(self, commit=True):
        fn, ln = self.cleaned_data['professor'].split()
        if Professor.objects.filter(first_name=fn, last_name=ln).exists():
            return Professor.objects.get(first_name=fn, last_name=ln)

        p = Professor(first_name=fn, last_name=ln)
        if commit:
            p.save()

        return p
