from __future__ import absolute_import

from .models import Textbook, Author, Semester, Professor

from django.contrib import admin


class AuthorInline(admin.TabularInline):
    model = Author


class SemesterAdmin(admin.ModelAdmin):
    pass


class ProfessorAdmin(admin.ModelAdmin):
    pass


class TextbookAdmin(admin.ModelAdmin):
    inlines = [
        AuthorInline,
    ]


admin.site.register(Textbook, TextbookAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Professor, ProfessorAdmin)
