'''
admin.py - это файл, в котором мы будем регистрировать наши модели для административного интерфейса.
'''

from django.contrib import admin

from post.models import Post, Comment, Tag


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
