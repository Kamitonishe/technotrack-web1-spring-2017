from __future__ import unicode_literals
from django.db import models
from application import settings
import post


class Comment(models.Model):
    text = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('post.Post')
    rate = models.IntegerField(default=0)