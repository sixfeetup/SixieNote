from django import forms
from django.forms.widgets import HiddenInput

from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        exclude = ['owner', 'pub_date']
