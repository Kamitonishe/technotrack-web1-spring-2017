from __future__ import unicode_literals
from django.db import models
from application import settings


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    rate = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

class BlogLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)