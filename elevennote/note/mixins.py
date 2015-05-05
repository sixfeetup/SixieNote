from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Note


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class NoteMixin(object):
    def get_context_data(self, **kwargs):
        context = super(NoteMixin, self).get_context_data(**kwargs)

        context.update({
            'notes': Note.objects.filter(owner=self.request.user).order_by('-pub_date'),
        })
        
        return context
