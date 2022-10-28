from django.urls import path
from django.views import View
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.my_logout, name='logout'), 
]