from django.conf.urls import url
from django.http import HttpResponseRedirect

from .views import NoteCreate, NoteUpdate, ProfileView

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('new/'), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', NoteUpdate.as_view(), name='update'),
    url(r'^new/$', NoteCreate.as_view(), name='create'),

    # This is probably more applicable in the root urls
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
]
