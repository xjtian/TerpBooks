from __future__ import absolute_import

from rest_framework import serializers

from .models import Textbook, Author, Semester, Professor


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


class TextbookRelatedSerializer(serializers.ModelSerializer):
    authors = serializers.RelatedField(many=True)
    semester = serializers.RelatedField()
    professor = serializers.RelatedField()

    class Meta:
        model = Textbook
