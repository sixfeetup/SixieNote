from django.contrib.auth.models import User
from rest_framework import serializers

from sixienote.note.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'pub_date', 'workflow_state')
        read_only_fields = ('workflow_state',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
