from django.conf.urls import url
from django.contrib import admin
from .views import RegisterFormView, UserView
from views import HomePageView
from  django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^user/$', UserView.as_view(), name='userpage'),

]