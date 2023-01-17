import time
from django.shortcuts import get_object_or_404, redirect, render
import urllib
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from clientes.forms import DateForm
from .models import Laudo, Mensage, Person
from django.views.generic.list import ListView
#from django.contrib.auth.mixins import LoginRequiredMixin
from gestor_laudo import scrapers

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

class LaudoCreate(CreateView):
    model = Laudo
    fields = ['numero','tipo','cliente', 'placa','dataLaudo','dataValidade']  
    success_url = reverse_lazy('laudo_list')

def LaudoList(request):         
    laudos = Laudo.objects.all().order_by('dataValidade')                
    for laudo in laudos:
        #aqui eu estou adicionando esses atributos só para a table                
        laudo.vencimento = laudo.get_days_left()
    return render(request, 'clientes/laudo_list.html', {'object_list':laudos})    
    
class LaudoUpdate(UpdateView):
    model = Laudo
    fields = ['numero','tipo','cliente', 'placa','dataLaudo','dataValidade'] 
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

def verify_mensage():    
    laudos = Laudo.objects.all()    
    for laudo in laudos:        
        msg = ''
        if (laudo.get_days_left() < 31):
            #verifica se já existe uma mensagem dessas no banco            
            vencimento = laudo.get_days_left()            
            #infelizment não sei como corrigir isso.
            mensagem = f"Olá estamos entrando em contato para lhe informar que o veículo: *{laudo.placa}*, estará com o *{laudo.tipo}* vencendo em {vencimento} dias. Venha à Agil Inspeções : Endereço: TO 080 - Luzimangues, Porto Nacional - TO. Abraço e tenha um bom dia" 
            
            if(Mensage.objects.filter(laudo = laudo, type="periodo1").exists()):
                print('Existe a mensagem')
            else:
                msg = Mensage(mensage = mensagem,phone = laudo.cliente.whatsapp,laudo = laudo,type = 'periodo1')
                Mensage.save(msg)
                        
def send_mensage():
    mensage = Mensage
    print('send messege')
    for mensage in mensage.objects.filter(send=False):
        #TODO aqui enviar um email se o whatsapp estiver offline o whatsapp;
        print('passou')
        if(scrapers.whats_login()):
            request = scrapers.send_messege(mensage.mensage, mensage.phone)
            if(request == 'msg ok'):
                mensage.send = True
                mensage.save()
            else:
                #TODO enviar email com o erro do número cadastrado.
                pass   