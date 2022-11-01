from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', PersonCreate.as_view(), name=""),   
    path('person_list/', login_required(PersonList.as_view()), name="person_list"),           
    path('person_create/', login_required(PersonCreate.as_view()), name="person_create"),           
    path('person_update/<int:pk>/', login_required(PersonUpdate.as_view()), name="person_update"),      
    path('person_delete/<int:pk>/', personDelete, name='person_delete'),    
    
    path('empresa_list/', login_required(EmpresaList.as_view()), name="empresa_list"),
    path('empresa_create/', login_required(EmpresaCreate.as_view()), name="empresa_create"),
    path('empresa_update/<int:pk>/', login_required(EmpresaUpdate.as_view()), name="empresa_update"),
    path('empresa_delete/<int:pk>/', EmpresaDelete, name="empresa_delete"),    
    
    path('laudo_list/', login_required(LaudoList.as_view()), name="laudo_list"),
    path('laudo_create/', login_required(LaudoCreate.as_view()), name="laudo_create"),
    path('laudo_update/<int:pk>/', login_required(LaudoUpdate.as_view()), name="laudo_update"),
    path('laudo_delete/<int:pk>/', LaudoDelete, name="laudo_delete"),        
    
    path('laudo_new/', login_required(Laudo_new), name="laudo_new"),
    
]


