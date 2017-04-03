from blog.views import BlogsList, BlogView
from .views import CommentView
from django.conf.urls import url,include


urlpatterns = [
    #url(r'^/new/$', CreateComment.as_view(), name='newcomment'),
]