from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Note


def index(request):
    latest_note_list = Note.objects.order_by('-pub_date')[:5]
    template = loader.get_template('note/index.html')
    context = RequestContext(request, {
        'latest_note_list': latest_note_list,
    })
    return HttpResponse(template.render(context))

def detail(request, note_id):
    return HttpResponse("You're looking at note %s." % note_id)
