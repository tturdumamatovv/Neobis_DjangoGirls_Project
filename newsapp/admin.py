from django.contrib import admin

from .models import News, Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'news')
