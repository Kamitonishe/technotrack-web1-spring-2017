from django.shortcuts import render, resolve_url, get_object_or_404
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

class PostDetail(CreateView):
    template_name = 'post/singlepost.html'
    model = Comment
    fields = ('text',)
    success_url = 'blog:blogs'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostDetail, self).form_valid(form)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context


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
