from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import BugReport, FeatureRequest

# def index(request):
#     bugs_page_url = reverse('quality_control:bug_list')
#     features_page_url = reverse('quality_control:feature_list')
#     html = f"<h1>Система контроля качества</h1>\
#     <li><a href='{bugs_page_url}'>Система контроля качества</a></li>\
#     <li><a href='{features_page_url}'>Запросы на улучшение</a></li>"
#     return HttpResponse(html)

# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
#     for bug in bugs:
#         bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
#     bugs_html += '</ul>'
#     return HttpResponse(bugs_html)

# def bag_detail(request, bug_id:int):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>\
#         <p>status: {bug.status}, priority: {bug.priority}</p> <p>project: {bug.project.name}</p> <p>task: {bug.task.name}</p>'
#     return HttpResponse(response_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


def feature_id_detail(request, feature_id:int):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>\
        <p>status: {feature.status}, priority: {feature.priority}</p> \
        <p>project: {feature.project.name}</p> <p>task: {feature.task.name}</p>'
    return HttpResponse(response_html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_control:bug_list')
        features_page_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1>\
        <li><a href='{bugs_page_url}'>Система контроля качества</a></li>\
        <li><a href='{features_page_url}'>Запросы на улучшение</a></li>"
        return HttpResponse(html)
    
class BugsListView(ListView):
    model = BugReport
    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)
    
class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>\
        <p>status: {bug.status}, priority: {bug.priority}</p> <p>project: {bug.project.name}</p> <p>task: {bug.task.name}</p>'
        return HttpResponse(response_html)
    
class FeaturesListView(ListView):
    model = FeatureRequest
    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список запросов на улучшение</h1><ul>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
        features_html += '</ul>'
        return HttpResponse(features_html)
    
class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>\
        <p>status: {feature.status}, priority: {feature.priority}</p> \
        <p>project: {feature.project.name}</p> <p>task: {feature.task.name}</p>'
        return HttpResponse(response_html)
