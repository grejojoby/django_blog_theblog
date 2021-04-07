from django.contrib import admin
from .models import Comments, Post, Category, Profile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comments)