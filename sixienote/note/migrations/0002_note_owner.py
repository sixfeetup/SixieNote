# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models, migrations
from django.db.models import CASCADE


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL, on_delete=CASCADE),
            preserve_default=False,
        ),
    ]
