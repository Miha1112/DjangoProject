from django.contrib import admin
from .models import Post, Comments, AboutUs


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Comments)
class CommentsAdmon(admin.ModelAdmin):
    list_display = ('name', 'post')


@admin.register(AboutUs)
class AboutUSAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gitLink', 'work', 'descr')
