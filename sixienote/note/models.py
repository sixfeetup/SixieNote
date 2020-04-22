# Python imports
from datetime import timedelta

# Django imports
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_fsm import FSMField, transition

# Create your models here.
from rest_framework.authtoken.models import Token


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('date published')
    workflow_state = FSMField(default='draft')

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

    @transition(field=workflow_state, source='draft', target='published')
    def publish(self):
        # send notification to websocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "workflow", {"type": "workflow.update",
                         "workflow_state": "published",
                         "note_id": self.id})

    @transition(field=workflow_state, source='published', target='draft')
    def retract(self):
        # send notification to websocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "workflow", {"type": "workflow.update",
                         "workflow_state": "draft",
                         "note_id": self.id})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

