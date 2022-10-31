from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Person
from django.views.generic.list import ListView
#from django.contrib.auth.mixins import LoginRequiredMixin

class PersonCreate(CreateView):
    model = Person
    fields = ['name','email', 'whatsapp']
    success_url = reverse_lazy('home')

class PersonList(ListView):
    model = Person

class PersonUpdate(UpdateView):
#    login_url = 'login'
    model = Person
    fields = ['name','email', 'whatsapp']
    success_url = reverse_lazy('home')
    
def personDelete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    #nesse eu envio uma pessoa para criar uma instância lá no template, para decidir se vou deletar.        
    person.delete()
    return redirect('person_list')