from django.conf.urls import url
from django.http import HttpResponseRedirect

from .views import NoteCreate, NoteUpdate

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('new/'), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='update'),
    url(r'^new/$', NoteCreate.as_view(), name='create'),
]
