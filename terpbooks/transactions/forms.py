from __future__ import absolute_import

from terpbooks.forms import BootstrapModelForm

from .models import Listing, TransactionRequest


class ListingForm(BootstrapModelForm):
    class Meta:
        model = Listing
        fields = ('asking_price', 'comments', )

    def save(self, commit=True, book=None, owner=None):
        listing = super(ListingForm, self).save(commit=False)

        if book is None:
            raise Exception('Cannot save listing without associated book.')
        if owner is None:
            raise Exception('Cannot save listing without associated owner.')

        listing.book = book
        listing.owner = owner
        if commit:
            listing.save()

        return listing


class TransactionRequestForm(BootstrapModelForm):
    class Meta:
        model = TransactionRequest
        fields = ('text', 'price', )

    def __init__(self, *args, **kwargs):
        super(TransactionRequestForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'rows': 5})

    def is_valid(self, thread=None, user=None):
        valid = super(TransactionRequestForm, self).is_valid()
        if not valid:
            return False

        if thread is not None and user is not None:
            # You're not allowed to create a request for your own listing
            if user == thread.listing.owner:
                return False

        return True

    def save(self, commit=True, thread=None, user=None):
        request = super(TransactionRequestForm, self).save(commit=False)

        if thread is None:
            raise Exception('Cannot save message without associated thread.')
        if user is None:
            raise Exception('Cannot save message without associated creator.')

        request.created_by = user
        request.thread = thread

        if commit:
            request.save()

        return request
