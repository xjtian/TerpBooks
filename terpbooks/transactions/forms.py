from __future__ import absolute_import

from terpbooks.forms import BootstrapModelForm

from .models import Listing


class ListingForm(BootstrapModelForm):
    class Meta:
        model = Listing
        fields = ('asking_price', 'comments', )

    def __init__(self, owner, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        self.owner = owner

    def save(self, commit=True):
        instance = super(ListingForm, self).save(commit=False)
        instance.owner = self.owner

        if commit:
            instance.save()

        return instance
