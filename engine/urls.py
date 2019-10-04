"""
main engine urls

"""
from django.contrib import admin
from django.urls import path, include
from portfolio import views as myapp_views
from django.conf.urls import handler404, handler500
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls'))
]

urlpatterns += staticfiles_urlpatterns()

handler404 = myapp_views.error_404
handler500 = myapp_views.error_500