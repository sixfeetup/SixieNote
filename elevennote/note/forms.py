from django import forms

from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        exclude = ['owner', 'pub_date']
