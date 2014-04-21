from __future__ import absolute_import

from django.views import generic
from django.shortcuts import render

from .forms import AuthorFormSet


class DynamicAuthorForms(generic.View):
    def post(self, request):
        """
        Binds posted data to an AuthorFormSet, then returns a new formset
        with the posted data and an extra blank form at the end.
        """
        posted_formset = AuthorFormSet(request.POST)

        initial = []
        for form in posted_formset:
            data = {}
            for field in form.fields:
                data[field] = form[field].value()
            initial.append(data)

        formset = AuthorFormSet(initial=initial)

        return render(request, 'sell/author_formset.html', {
            'author_formset': formset,
        })
