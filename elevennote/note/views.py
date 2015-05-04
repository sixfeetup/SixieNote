from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Note


def index(request):
    latest_note_list = Note.objects.order_by('-pub_date')[:5]
    context = {
        'latest_note_list': latest_note_list,
    }
    return render(request, 'note/index.html', context)

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note/detail.html', {'note': note})
