'''
admin.py - это файл, в котором мы будем регистрировать наши модели для административного интерфейса.
'''

from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from post.models import Post, Comment, Tag


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at', 'rate', 'id')
    # fields = ('id', 'title', 'content', 'rate', 'tags', 'created_at', 'updated_at')

    # fieldsets = (
    #     ("General", {
    #         'fields': ('title', 'content', 'tags')
    #     }),
    #     ('Readonly Fields', {
    #         'fields': ('id', 'rate', 'created_at', 'updated_at'),
    #         # 'classes': ('collapse',)
    #     }),
    # )

    def save_model(self, request, obj, form, change):
        obj.title = obj.title.capitalize()
        super().save_model(request, obj, form, change)
    
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(rate=0)
    
    # def has_add_permission(self, request):
    #     if Post.objects.count() >= 10:
    #         return False
    #     return True
    
    # def has_change_permission(self, request, obj=None):
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Comment)
admin.site.register(Tag)
