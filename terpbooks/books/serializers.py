from __future__ import absolute_import

from .models import Textbook, Author, Semester, Professor

from rest_framework import serializers


class TextbookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True)
    semester = serializers.PrimaryKeyRelatedField()
    professor = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Textbook


class AuthorSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(required=True)

    class Meta:
        model = Author


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
