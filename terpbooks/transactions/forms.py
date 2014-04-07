from __future__ import absolute_import

from terpbooks.forms import BootstrapModelForm

from .models import Listing


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
