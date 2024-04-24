from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_url = reverse('quality_control:quality_control')
    html = f"<h1>Страница приложения tasks</h1>\
        <a href='{another_page_url}'>Перейти на другую страницу</a>\
        <a href='{quality_control_url}'>Перейти на страницу контроля качества</a>"
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")

    