from django.shortcuts import render
from django.http import HttpResponse

from .models import Note


def index(request):
    latest_note_list = Note.objects.order_by('-pub_date')[:5]
    context = {
        'latest_note_list': latest_note_list,
    }
    return render(request, 'note/index.html', context)

def detail(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")

    return render(request, 'note/detail.html', {'note': note})
