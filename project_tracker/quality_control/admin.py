from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.action(description="Change status to New")
def make_new(modeladmin, request, queryset):
    queryset.update(status='New')

@admin.action(description="Change status to In progress")
def make_in_progress(modeladmin, request, queryset):
    queryset.update(status='In_progress')

@admin.action(description="Change status to Completed")
def make_complited(modeladmin, request, queryset):
    queryset.update(status='Completed')


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'project', 'task')
    ordering = ('priority',)
    list_filter = ('project', 'task', 'priority', 'status')
    list_editable = ('project', 'task', 'status', 'priority')
    readonly_fields = ('created_at', 'updated_at')

    actions = [make_new, make_in_progress, make_complited]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'task', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'project', 'task')
    ordering = ('priority',)
    list_filter = ('project', 'task', 'priority', 'status')
    readonly_fields = ('created_at', 'updated_at')