from __future__ import absolute_import

from django.views import generic
from django.forms.formsets import formset_factory
from django.shortcuts import render

from .forms import AuthorForm, AuthorFormSet


class AuthorFormSetView(generic.View):
    def get(self, request, *args, **kwargs):
        n = kwargs.pop('count', '1')
        if len(n) == 0:
            n = '1'

        n = int(n)
        n = max(n, 1)

        formset = formset_factory(AuthorForm, AuthorFormSet, extra=n)()
        return render(request, 'sell/author_formset.html', {
            'formset': formset
        })
