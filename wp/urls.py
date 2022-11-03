from django.urls import path
from django.views import View
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [    
    path('status/', views.myView, name='status'), 
    path('send_Message/', views.createMessage, name='send_1'), 
    path('vencimento/', views.vencimento, name='vencimento'), 
    path('send/<int:pk>/', views.prepareMessage, name='prepare'),
    path('send/', views.sendMessage, name="send"),
]
