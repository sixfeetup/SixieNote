from tastypie.resources import ModelResource
from ..models import Note


class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        allowed_methods = ['get']
