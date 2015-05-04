# Python imports
from datetime import timedelta

# Django imports
from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)
