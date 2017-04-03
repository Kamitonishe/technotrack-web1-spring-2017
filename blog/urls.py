from django.conf.urls import url, include
from django.contrib import admin
from blog.views import BlogView, BlogsList, CreateBlog
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^/$', BlogsList.as_view(), name="blogs"),
    url(r'^/(?P<pk>\d+)/$', BlogView.as_view(), name="singleblog"),
    url(r'^/new/$', login_required(CreateBlog.as_view()), name="newblog"),



]