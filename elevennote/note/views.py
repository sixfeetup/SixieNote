from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from .models import Note
from .mixins import LoginRequiredMixin
from .forms import NoteForm

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


class NoteCreate(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    template_name = 'note/form.html'
    success_url = reverse_lazy('note:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.pub_date = timezone.now()
        return super(NoteCreate, self).form_valid(form)
