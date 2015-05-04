from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the notes index.")

def detail(request, note_id):
    return HttpResponse("You're looking at note %s." % note_id)
