from __future__ import absolute_import

from rest_framework import viewsets

from .models import Textbook, Author, Semester, Professor
from .serializers import TextbookSerializer, AuthorSerializer, SemesterSerializer, ProfessorSerializer


class TextbookViewSet(viewsets.ModelViewSet):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    # TODO: filter semesters chronologically
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


# TODO: static API view to reveal full names of semester choice field options