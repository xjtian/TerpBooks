from django.db import models


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

    year = models.IntegerField()
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
    edition = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=13, blank=True)

    course_code = models.CharField(max_length=20, blank=True)
    semester = models.ForeignKey(Semester, null=True, blank=True)
    professor = models.ForeignKey(Professor, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    def authors_string(self):
        """
        Returns Unicode string with list of authors
        """
        all_authors = Author.objects.filter(book=self).order_by('last_name')
        return u', '.join([unicode(a) for a in all_authors])


class Author(models.Model):
    """
    Author of a book.
    """
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

    book = models.ForeignKey(Textbook, related_name='authors')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
