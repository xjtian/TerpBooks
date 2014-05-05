from django.db.models import Q

from django.views import generic

from transactions.models import TransactionRequestThread


def unread_messages(user):
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
    Splash page view
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(SplashPage, self).get_context_data(**kwargs)
        context.update({'banner': True, 'unread': unread_messages(self.request.user)})

        return context