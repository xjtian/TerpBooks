from __future__ import absolute_import

from rest_framework import viewsets, views
from rest_framework.response import Response

from .models import Textbook, Author, Semester, Professor
from .serializers import TextbookSerializer, AuthorSerializer, SemesterSerializer, ProfessorSerializer


class TextbookViewSet(viewsets.ModelViewSet):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all().order_by('-year', 'semester')
    serializer_class = SemesterSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class SemesterChoiceLookup(views.APIView):
    """
    View for looking up the long names of semester choices.
    """
    def get(self, request, format=None):
        choices = Semester.SEMESTER_CHOICES

        forward = {x: y for (x, y) in choices}
        backward = {y: x for (x, y) in choices}

        obj = {'forward': forward, 'reverse': backward}
        return Response(obj)
