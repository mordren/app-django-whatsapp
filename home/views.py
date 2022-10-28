from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):         
    #import pdb; pdb.set_trace()
    return render(request, 'home/home.html')

def my_logout(request):
    logout(request)
    return redirect('home')

