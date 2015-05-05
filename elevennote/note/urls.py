from django.conf.urls import url

from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate

urlpatterns = [
    url(r'^$', NoteList.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', NoteDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', NoteUpdate.as_view(), name='update'),
    url(r'^new/$', NoteCreate.as_view(), name='create'),
]
