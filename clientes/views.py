from typing import List
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from clientes.forms import DateForm
from .models import Empresa, Laudo, Person
from django.views.generic.list import ListView
#from django.contrib.auth.mixins import LoginRequiredMixin

class PersonCreate(CreateView):
    model = Person
    fields = ['name','email', 'whatsapp']
    success_url = reverse_lazy('person_list')

class PersonList(ListView):
    model = Person

class PersonUpdate(UpdateView):
#    login_url = 'login'
    model = Person
    fields = ['name','email', 'whatsapp']
    success_url = reverse_lazy('person_list')
    
def personDelete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    #nesse eu envio uma pessoa para criar uma instância lá no template, para decidir se vou deletar.        
    person.delete()
    return redirect('person_list')

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name','telefone','whatsapp']
    success_url = reverse_lazy('home')

class EmpresaList(ListView):
    model = Empresa
    
class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['name','telefone','whatsapp']
    success_url = reverse_lazy('empresa_list')
    
def EmpresaDelete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    #nesse eu envio uma pessoa para criar uma instância lá no template, para decidir se vou deletar.        
    empresa.delete()
    return redirect('empresa_list')

class LaudoCreate(CreateView):
    model = Laudo
    fields = ['numero','tipo','cliente', 'empresa','dataValidade']  
    success_url = reverse_lazy('laudo_list')

class LaudoList(ListView):
    model = Laudo
    
class LaudoUpdate(UpdateView):
    model = Laudo
    fields = ['numero','tipo','cliente', 'empresa', 'dataValidade']
    success_url = reverse_lazy('laudo_list')
    
def LaudoDelete(request, pk):
    laudo = get_object_or_404(Laudo, pk=pk)
    #nesse eu envio uma pessoa para criar uma instância lá no template, para decidir se vou deletar.        
    laudo.delete()
    return redirect('laudo_list')

def Laudo_new(request):
    form = DateForm(request.POST or None, request.FILES or None)  
    if form.is_valid():        
        form.save()
        return redirect('laudo_list')
    return render(request, 'clientes/laudo_form.html', {'form':form})