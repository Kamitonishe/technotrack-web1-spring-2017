from django.shortcuts import render, resolve_url
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from blog.models import Blog
from post.models import Post
from comment.models import Comment
from django.views.generic.base import TemplateView
from django import forms


class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post/singlepost.html'


class CreatePost(CreateView):
    template_name = 'post/newpost.html'
    model = Post
    fields = ('text', 'title', 'blog')
    success_url = 'blog:blogs'

    def get_success_url(self):
        return resolve_url('blog:singleblog', pk=self.object.blog.pk)

    def get_form(self, form_class=None):
        form = super(CreatePost, self).get_form()
        form.fields['blog'].queryset = Blog.objects.all().filter(author=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)




class UpdatePost(UpdateView):

    template_name = 'post/editpost.html'
    model = Post
    fields = ('text', 'blog')
    success_url = '/blogs/'

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


#class BlogForm(forms.ModelForm):
#    class Meta:
#        model = Blog
#        fields = ('title','description','rate')
