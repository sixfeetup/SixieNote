from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from .models import Note
from .mixins import LoginRequiredMixin, NoteMixin
from .forms import NoteForm


class NoteCreate(LoginRequiredMixin, NoteMixin, CreateView):
    form_class = NoteForm
    template_name = 'note/form.html'
    success_url = reverse_lazy('note:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.pub_date = timezone.now()
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, NoteMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note/form.html'
    success_url = reverse_lazy('note:index')

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super(NoteUpdate, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.check_user_or_403(self.object.owner)
        return super(NoteUpdate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.check_user_or_403(self.object.owner)
        return super(NoteUpdate, self).post(request, *args, **kwargs)


class NoteDelete(LoginRequiredMixin, NoteMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note:index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.check_user_or_403(self.object.owner)
        return super(NoteDelete, self).post(request, *args, **kwargs)
