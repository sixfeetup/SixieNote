from django.views.generic import ListView, DetailView

from .models import Note
from .mixins import LoginRequiredMixin


class NoteList(LoginRequiredMixin, ListView):
    paginate_by = 5
    template_name = 'note/index.html'
    context_object_name = 'latest_note_list'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'

