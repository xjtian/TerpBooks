from django.db import models
from django.conf import settings

from books.models import Textbook


class Listing(models.Model):
    """
    Listing for a textbook.
    """
    AVAILABLE = 'AV'
    PENDING = 'PN'
    SOLD = 'SD'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (PENDING, 'Transaction Pending'),
        (SOLD, 'Sold'),
    )

    date_created = models.DateField(auto_now_add=True, editable=False)

    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=AVAILABLE)
    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')

    book = models.OneToOneField(Textbook, related_name='listing')
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.book.title, self.get_status_display())


class TransactionRequestThread(models.Model):
    """
    Container for replies to/about a transaction request.
    """
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests')
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    listing = models.ForeignKey(Listing, related_name='requests')

    def __unicode__(self):
        return u'%s' % self.listing.book.title


class TransactionRequest(models.Model):
    """
    Transaction request for a textbook.
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_messages')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField(blank=True)

    thread = models.ForeignKey(TransactionRequestThread, related_name='messages')
