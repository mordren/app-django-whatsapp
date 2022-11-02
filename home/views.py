from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from gestor_laudo.scrapers import *

# Create your views here.
@login_required(login_url='login')
def home(request):         
    #import pdb; pdb.set_trace()    
    whats = WhatsStatus()   
    return render(request, 'home/home.html', {'whats':whats})

def my_logout(request):
    logout(request)
    return redirect('home')