from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='quality_control'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bag_detail, name='bag_detail'),
    # path('features/<int:feature_id>/', views.feature_id_detail, name='featur_detail'),

    path('', views.IndexView.as_view(), name='quality_control'),
    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    path('features/', views.FeaturesListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bag_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='featur_detail'),

]