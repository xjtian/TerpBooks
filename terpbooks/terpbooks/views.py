from django.views import generic
from django.shortcuts import render
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required


class BuyPage(generic.View):
    """
    Buy page view.
    """
    def get(self, request):
        return render(request, 'buy/index.html', {
            'active': 'buy',
        })


class ProfilePage(generic.View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'profile/index.html', {
            'active': 'profile',
        })