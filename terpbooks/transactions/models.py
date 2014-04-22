from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

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
    asking_price = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       validators=[MinValueValidator(0)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')

    book = models.OneToOneField(Textbook, related_name='listing')
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.book.title, self.get_status_display())

    def request_count(self):
        """
        Returns the number of transaction requests for this listing.
        """
        return self.requests.count()

    def unread_messages(self):
        """
        Returns the number of unread transaction messages for this listing.
        """
        return sum(map(lambda l: l.unread_messages_seller(), self.requests.all()))

    def is_sold(self):
        return self.status == Listing.SOLD

    def is_pending(self):
        return self.status == Listing.PENDING

    def is_available(self):
        return self.status == Listing.AVAILABLE


class TransactionRequestThread(models.Model):
    """
    Container for replies to/about a transaction request.
    """
    # The sender is the potential buyer
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests')
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    listing = models.ForeignKey(Listing, related_name='requests')

    def __unicode__(self):
        return u'%s' % self.listing.book.title

    def unread_messages_seller(self):
        """
        How many unread messages in this thread the seller has.
        """
        return self.messages.filter(created_by=self.sender, read=False).count()

    def unread_messages_buyer(self):
        """
        How many unread messages in this thread the buyer has.
        """
        return self.messages.exclude(created_by=self.sender).filter(read=False).count()

    def last_buyer_offer_price(self):
        """
        Value of the last offer sent by the buyer.
        """
        qs = self.messages.filter(created_by=self.sender).order_by('-date_created')
        price = 0.00

        if qs.exists():
            price = qs[0].price

        return price

    def last_buyer_offer_time(self):
        """
        Returns the time that the last buyer offer was made.
        """
        qs = self.messages.filter(created_by=self.sender).order_by('-date_created')
        time = None

        if qs.exists():
            time = qs[0].date_created

        return time


    def last_seller_offer_time(self):
        """
        Returns the time that the last seller counteroffer was made,
        or None if no counteroffers are in this thread yet.
        """
        qs = self.messages.exclude(created_by=self.sender).order_by('-date_created')
        time = None

        if qs.exists():
            time = qs[0].date_created

        return time

    def last_seller_offer_price(self):
        """
        Value of the last counteroffer sent by the seller.
        """
        qs = self.messages.exclude(created_by=self.sender).order_by('-date_created')
        price = 0.00

        if qs.exists():
            price = qs[0].price

        return price

    def last_message_time(self):
        """
        Time of the most recent message by either the seller or buyer.
        """
        qs = self.messages.order_by('-date_created')
        time = None

        if qs.exists():
            time = qs[0].date_created

        return time

    def chron_messages(self):
        """
        Return all messages in this thread chronologically.
        """
        return self.messages.order_by('date_created')

    def mark_seen_by(self, user):
        """
        Mark all messages in thread not sent by provided user as read.
        """
        qs = self.messages.exclude(created_by=self.sender)
        seller = None
        if qs.exists():
            seller = qs[0].created_by

        if user != self.sender:
            if seller is not None and user != seller:
                return

        qs = self.messages.exclude(created_by=user).filter(read=False)
        for message in qs:
            message.read = True
            message.save()


class TransactionRequest(models.Model):
    """
    Transaction request for a textbook.
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_messages')
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[MinValueValidator(0)])
    text = models.TextField(blank=True)
    read = models.BooleanField(default=False)

    thread = models.ForeignKey(TransactionRequestThread, related_name='messages')
