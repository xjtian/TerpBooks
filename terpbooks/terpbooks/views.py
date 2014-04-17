from django.views import generic
from django.shortcuts import render


class BuyPage(generic.View):
    """
    Buy page view.
    """
    def get(self, request):
        return render(request, 'buy/index.html', {
            'active': 'buy',
        })


class ProfilePage(generic.View):
    def get(self, request):
        return render(request, 'profile/index.html', {
            'active': 'profile',
        })