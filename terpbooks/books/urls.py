from __future__ import absolute_import

from rest_framework import routers

from .views import TextbookViewSet, AuthorViewSet, SemesterViewSet, ProfessorViewSet


router = routers.SimpleRouter()
router.register(r'books', TextbookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'professors', ProfessorViewSet)

urlpatterns = router.urls
