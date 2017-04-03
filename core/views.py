#coding: utf-8
from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from models import UserRegistration
from blog.models import Blog
from post.models import Post
from comment.models import Comment
from django.views.generic.base import TemplateView



class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blog_count'] = Blog.objects.all().filter(author=self.request.user).count()
        context['post_count'] = Post.objects.all().filter(author=self.request.user).count()
        context['comment_count'] = Comment.objects.all().filter(author=self.request.user).count()
        return context

class RegisterFormView(FormView):
    form_class = UserRegistration
    success_url = "/"
    template_name = "core/register.html"

    def get_success_url(self):
        return resolve_url('core:home')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class UserView(TemplateView):
    template_name = 'core/userpage.html'