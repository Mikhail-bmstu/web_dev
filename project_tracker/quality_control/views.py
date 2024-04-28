from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import BugReport, FeatureRequest
from django.template.loader import render_to_string
from .forms import BugReportForm, FeatureRequestForm

# def index(request):
#     template = render_to_string('quality_control/index.html')
#     return HttpResponse(template)

# def bug_list(request):
#     bugs = BugReport.objects.all()
#     return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

# def bug_detail(request, bug_id:int):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     return render(request, 'quality_control/bug_detail.html', {'bug': bug})

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     return render(request, 'quality_control/feature_list.html', {'feature_list': features})


# def feature_detail(request, feature_id:int):
#     feature = get_object_or_404(FeatureRequest, id=feature_id)
#     return render(request, 'quality_control/feature_detail.html', {'feature': feature})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
    
class BugsListView(ListView):
    model = BugReport
    context_object_name = 'bug_list'
    template_name = 'quality_control/bug_list.html'
    
class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'
    
class FeaturesListView(ListView):
    model = FeatureRequest
    context_object_name = 'feature_list'
    template_name = 'quality_control/feature_list.html'
    
class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'

def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})
