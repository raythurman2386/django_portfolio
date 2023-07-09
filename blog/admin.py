from django.contrib import admin
from .models import Hero, Category, Tag, Post, Comment, Contact
# Register your models here.

admin.site.register(Hero)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
