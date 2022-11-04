from django.urls import path
from django.views import View
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [    
    path('status/', login_required(views.status), name='status'),     
    path('vencimento/', login_required(views.vencimento), name='vencimento'), 
    path('send/<int:pk>/', login_required(views.prepareMessage), name='prepare'),
    path('send/', login_required(views.sendMessage), name="send"),
]
