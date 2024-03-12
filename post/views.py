'''
HTTP methods:
    - GET: retrieve data from the server
    - POST: send data to the server
    - PUT: update data on the server
    - DELETE: delete data from the server
'''
import random

from django.shortcuts import render
from django.http import HttpResponse


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


