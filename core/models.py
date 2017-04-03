from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)