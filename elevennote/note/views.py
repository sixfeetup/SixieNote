from django.views.generic import CreateView, UpdateView
from django.views.generic.list import BaseListView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

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

        if self.object.owner != self.request.user:
            raise PermissionDenied

        return super(NoteUpdate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.owner != self.request.user:
            raise PermissionDenied

        return super(NoteUpdate, self).post(request, *args, **kwargs)


class JSONListView(LoginRequiredMixin, BaseListView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-pub_date'),

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        notes = []
        for note in self.object_list[0]:
            notes.append({
                'title': note.title,
                'body': note.body,
                'pub_date': note.pub_date,
            })

        response = {
            'user': self.request.user.username,
            'notes': notes,
            'count': len(notes),
        }
        
        return JsonResponse(response, **kwargs)

