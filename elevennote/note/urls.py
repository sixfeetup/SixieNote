from django.conf.urls import url
from django.http import HttpResponseRedirect

from .views import NoteCreate, NoteUpdate, NoteDelete, JSONListView

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('new/'), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='update'),
    url(r'^new/$', NoteCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/delete/$', NoteDelete.as_view(), name='delete'),

    # API
    url(r'^api/v1/list/$', JSONListView.as_view(), name='json-list')
]
