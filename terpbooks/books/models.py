from datetime import date

from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Semester(models.Model):
    """
    A semester of some school year.
    """
    FALL = 'CFL'
    SPRING = 'ASP'
    WINTER = 'DWN'
    SUMMER = 'BSM'

    SEMESTER_CHOICES = (
        (FALL, 'Fall'),
        (SPRING, 'Spring'),
        (WINTER, 'Winter'),
        (SUMMER, 'Summer'),
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(date.today().year + 1)
        ])

    semester = models.CharField(max_length=3,
                                choices=SEMESTER_CHOICES,
                                default=FALL)

    class Meta:
        unique_together = (('year', 'semester'),)

    def __unicode__(self):
        return u'%s %d' % (self.get_semester_display(), self.year)


class Professor(models.Model):
    """
    A unique professor represented by a first name and last name.
    """
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    class Meta:
        unique_together = (('first_name', 'last_name',),)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Textbook(models.Model):
    """
    Information about a textbook.
    """
    title = models.CharField(max_length=200, blank=False)
    edition = models.IntegerField(null=True,
                                  blank=True,
                                  validators=[MinValueValidator(1)])
    isbn = models.CharField(max_length=13,
                            blank=True,
                            validators=[RegexValidator(
                                regex=r'^[0-9 \-]*$',
                                message="Only numbers, dashes, and spaces are allowed in ISBN's."
                            )])

    course_code = models.CharField(max_length=20,
                                   blank=True,
                                   validators=[RegexValidator(
                                       regex=r'^[A-Z]{4}[0-9]{3}[A-Z]?$',
                                       message="Course codes must be formatted like 'ABCD123' or 'ABCD123E'"
                                   )])
    semester = models.ForeignKey(Semester, null=True, blank=True)
    professor = models.ForeignKey(Professor, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    def authors_string(self):
        """
        Returns Unicode string with list of authors
        """
        all_authors = Author.objects.filter(book=self).order_by('last_name')
        if not all_authors.exists():
            return u'Not provided'

        return u', '.join([unicode(a) for a in all_authors])


class Author(models.Model):
    """
    Author of a book.
    """
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    book = models.ForeignKey(Textbook, related_name='authors')

    class Meta:
        unique_together = (('first_name', 'last_name', 'book'),)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
