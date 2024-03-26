'''
HTTP methods:
    - GET: retrieve data from the server
    - POST: send data to the server
    - PUT: update data on the server
    - DELETE: delete data from the server
'''
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse

from post.models import Post, Comment
from post.forms import PostForm, PostForm2


def hello_view(request):
    random_number = random.randint(1, 100)
    if request.method == 'GET':
        return HttpResponse('Hello, World!' + str(random_number))


def main_page_view(request):
    MOCK_DATA = [
        {
            'id': 1,
            'name': 'John',
            'age': 25
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 30
        },
        {
            'id': 3,
            'name': 'Bob',
            'age': 35
        }
    ]

    context = {'name': 'Esen', 'mock_data': MOCK_DATA}
    if request.method == 'GET':
        return render(request, 'main.html', context=context)


def post_list_view(request):
    # 1. Достаем все посты из базы данных
    posts = Post.objects.all() # QuerySet
    # SELECT * FROM post_post;
    
    # 2. Передаем посты в контекст
    context = {'posts': posts}

    # 3. Отображаем шаблон
    return render(request, 'post/post_list.html', context)


def post_detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, 'errors/404.html')

    context = {'post': post}

    return render(request, 'post/post_detail.html', context)


def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'post/post_create.html', {'form': form})
    
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        # form.add_error('content', 'Текст не должен содержать слово Python!')

        if not form.is_valid():
            return render(request, 'post/post_create.html', {'form': form})

        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        image = form.cleaned_data.get('image')
        rate = form.cleaned_data.get('rate')
        tags = form.cleaned_data.get('tags')

        post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            rate=rate,
        )

        post.tags.set(tags)
        # post.tags.add(1)
        post.save()

        return redirect('post_list')
