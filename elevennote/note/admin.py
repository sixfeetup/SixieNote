from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

# Register your models here.
admin.site.register(Note, NoteAdmin)
