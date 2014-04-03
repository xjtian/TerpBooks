from __future__ import absolute_import

from terpbooks.forms import BootstrapModelForm

from .models import Listing


class ListingForm(BootstrapModelForm):
    class Meta:
        model = Listing
        fields = ('asking_price', 'comments', )
