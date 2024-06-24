from django.contrib import admin
from django.urls import path, include
from django.template.loader import render_to_string
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda response: HttpResponse(render_to_string('base/base.html')), name='home_page'),
    path("tasks/", include('tasks.urls')),
    path("quality_control/", include('quality_control.urls')),
    path('users/', include('users.urls')),
]
