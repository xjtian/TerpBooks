from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic

from transactions.models import TransactionRequestThread


def unread_messages(user):
    if user is None or not user.is_authenticated():
        return 0

    invovled_threads = TransactionRequestThread.objects.filter(Q(listing__owner=user) | Q(sender=user))
    count = 0

    for thread in invovled_threads:
        count += thread.messages.exclude(created_by=user).filter(read=False).count()

    return count


class BuyPage(generic.TemplateView):
    """
    Buy page view.
    """
    template_name = 'buy/index.html'

    def get_context_data(self, **kwargs):
        context = super(BuyPage, self).get_context_data(**kwargs)
        context.update({'active': 'buy', 'unread': unread_messages(self.request.user)})

        return context


class ProfilePage(generic.TemplateView):
    """
    Profile page view.
    """
    template_name = 'profile/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context.update({'active': 'profile', 'unread': unread_messages(self.request.user)})

        return context


class SplashPage(generic.TemplateView):
    """
    Splash page view - redirects to profile page if session user is authenticated.
    """
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated():
            return HttpResponseRedirect(reverse('profile'))

        return super(SplashPage, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SplashPage, self).get_context_data(**kwargs)
        context.update({'banner': True, 'unread': unread_messages(self.request.user)})

        return context