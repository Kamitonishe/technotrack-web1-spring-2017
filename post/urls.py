from django.conf.urls import url, include
from django.contrib import admin
from .models import Post
from post.views import PostView, CreatePost, UpdatePost
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^/(?P<pk>\d+)/$', PostView.as_view(), name="singlepost"),
    url(r'^/new$', login_required(CreatePost.as_view()), name="newpost"),
    url(r'^/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),
]

