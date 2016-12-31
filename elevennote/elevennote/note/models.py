# Python imports
from datetime import timedelta

# Django imports
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
