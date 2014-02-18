from __future__ import absolute_import

from rest_framework import viewsets

from .models import Textbook, Author, Semester, Professor
from .serializers import TextbookSerializer, AuthorSerializer, SemesterSerializer, ProfessorSerializer


class TextbookViewset(viewsets.ModelViewSet):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SemesterViewset(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class ProfessorViewset(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
