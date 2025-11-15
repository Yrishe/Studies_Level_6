from django.urls import path, re_path

from . import views

urlpatterns = [
    path('simple', helloworld_web_dev.views.simple_view, name='simple'),
    path('', views.index, name='index'),
]