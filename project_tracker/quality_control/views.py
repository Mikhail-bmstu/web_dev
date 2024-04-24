from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    bugs_page_url = reverse('quality_control:bug_list')
    features_page_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1>\
    <a href='{bugs_page_url}'>Система контроля качества</a>\
    <a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def bag_detail(request, id:int):
    return HttpResponse(f"Детали бага  {id}")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def feature_id_detail(request, id:int):
    return HttpResponse(f"Детали улучшения  {id}")
