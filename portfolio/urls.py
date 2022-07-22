# from django.conf.urls import url
from django.urls import path, include,re_path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('photos', views.photos, name='photos'),
    re_path(r'^api/projects/$', views.ProjectList.as_view()),
    re_path(r'^api-token-auth/', obtain_auth_token),
    re_path(r'api/project/project-id/(?P<pk>[0-9]+)/$', views.ProjectDescription.as_view()),
]
