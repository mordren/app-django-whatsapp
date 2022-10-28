from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', PersonCreate.as_view(), name=""),   
    path('list/', login_required(PersonList.as_view()), name="person_list"),           
    path('new/', login_required(PersonCreate.as_view()), name="person_create"),           
    path('update/<int:pk>/', login_required(PersonUpdate.as_view()), name="person_update"),      
    path('person_delete/<int:pk>/', personDelete, name='person_delete'),        
]


