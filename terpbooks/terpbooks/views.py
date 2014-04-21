from django.views import generic


class BuyPage(generic.TemplateView):
    """
    Buy page view.
    """
    template_name = 'buy/index.html'

    def get_context_data(self, **kwargs):
        context = super(BuyPage, self).get_context_data(**kwargs)
        context.update({'active': 'buy'})

        return context


class ProfilePage(generic.TemplateView):
    """
    Profile page view.
    """
    template_name = 'profile/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context.update({'active': 'profile'})

        return context
