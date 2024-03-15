from django.contrib import admin
from django.urls import path

from post.views import hello_view, main_page_view, post_list_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view, name='main_page'),
    path('hello/', hello_view, name='hello'),
    path('posts/', post_list_view, name='post_list')
]
