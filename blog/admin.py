from django.contrib import admin
from .models import Blog, BlogLike, Category

admin.site.register(Blog)
admin.site.register(BlogLike)
admin.site.register(Category)