from __future__ import unicode_literals
from django.db import models
from application import settings
import blog

class Post(models.Model):
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blog.Blog')
    rate = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class PostLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)