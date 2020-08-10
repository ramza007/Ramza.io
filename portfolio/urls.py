from django.conf.urls import url
from django.urls import path, include,re_path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('photos', views.photos, name='photos'),
    re_path(r'^api/projects/$', views.ProjectList.as_view()),
]
