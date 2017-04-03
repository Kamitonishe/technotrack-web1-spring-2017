from django.shortcuts import render, resolve_url
from django.views.generic import DetailView, ListView
from .models import Comment
from post.models import Post
from django.views.generic import DetailView, ListView, UpdateView, CreateView

class CommentView(DetailView, CreateView):
    queryset = Post.objects.all()
    model = Comment
    template_name = 'comments/comment.html'
    fields = ('title', 'description')
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CommentView, self).form_valid(form)

class CreateComment(CreateView):
    template_name = 'comment/newcomment.html'
    model = Comment
    fields = ('text', 'post')
    success_url = 'blog:blogs'

    def get_success_url(self):
        return resolve_url('post:singlepost', pk=self.object.post.pk)

    def get_form(self, form_class=None):
        form = super(CreateComment, self).get_form()
        form.fields['post'].queryset = Post.objects.all() #.filter(author=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateComment, self).form_valid(form)