#coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from .models import Blog, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth import get_user_model


class BlogsList(ListView):
    queryset = Blog.objects.all().order_by('created_date', 'title')
    template_name = 'blog/blogs.html'
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = SortForm()
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'blog/singleblog.html'


class CreateBlog(CreateView):
    category = models.ManyToManyField(Category)
    template_name = 'blog/newblog.html'
    model = Blog
    fields = ('title', 'text','categories')
    success_url = '/blogs/'

    def get_success_url(self):
        return resolve_url('blog:blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)


class UpdateBlog(UpdateView):
    template_name = 'post/editblog.html'
    model = Blog
    fields = ('title', 'text', 'categories')
    success_url = '/blogs/'
    category = models.ManyToManyField(Category)

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class SortForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('rate', u'Рейтинг'),
        ('created_date', u'Дата'),

    ))
    search = forms.CharField(required=False)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','text','rate')

class CreateUser(CreateView):
    model=get_user_model()
    template_name = 'core/register.html'
    fields = ('title', 'text')
    success_url = 'core/login/'