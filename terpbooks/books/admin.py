from __future__ import absolute_import

from .models import Textbook, Author, Semester, Professor

from django.contrib import admin


class AuthorInline(admin.TabularInline):
    model = Author


class SemesterInline(admin.TabularInline):
    model = Semester


class ProfessorInline(admin.TabularInline):
    model = Professor


class TextbookAdmin(admin.ModelAdmin):
    inlines = [
        AuthorInline,
        SemesterInline,
        ProfessorInline,
    ]


admin.site.register(Textbook, TextbookAdmin)
