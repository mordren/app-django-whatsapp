from datetime import date, timedelta
from datetime import datetime
from django.shortcuts import render
from clientes.models import Laudo
from gestor_laudo import scrapers
from django.shortcuts import get_object_or_404

# Create your views here.
def myView(request):
    #import pdb; pdb.set_trace()    
    #whats = WhatsStatus()       
    if (scrapers.whatsLogin()):
        return render(request, 'wp/status.html', {'status':True})
    else:        
        scrapers.importWhatsappQrCode()
        return render(request, 'wp/status.html', {'status':False})
    
def createMessage(request):
    print('')
    try:
        if request.method == 'POST':
            test = request.POST.get("number")           
            print(test)
            return render(request, 'wp/send.html', {'envio':''})                    
        else:
            return render(request, 'wp/send.html', {'envio':''})
        
        #envio = scrapers.sendMessage('teste automático',45998364044)
        #return render(request, 'wp/send.html', {'envio':envio})        
    except:
        return render(request, 'wp/send.html', {'envio':'erro'})        

def vencimento(request):
    laudos = Laudo.objects.all()                
    for laudo in laudos:
        laudo.telefone = getLaudoNumber(laudo)            
        laudo.vencimento = getDaysLeft(laudo)        
    return render(request, 'wp/vencimento.html', {'laudos':laudos})

def prepareMessage(request, pk):
    laudo = get_object_or_404(Laudo, pk=pk)    
    laudo.telefone = getLaudoNumber(laudo)            
    laudo.vencimento = getDaysLeft(laudo)           
    laudo.mensagem = f"Olá estamos entrando em contato para lhe informar que o veículo: *{laudo.placa}*, estará com o *{laudo.tipo}* vencendo em {laudo.vencimento} dias. Venha à Agil Inspeções : Endereço bla bla bla, Palmas-TO. Abraço e tenha um bom dia"
    return render(request, 'wp/send.html',{'laudo':laudo})

def sendMessage(request):    
    if (scrapers.whatsLogin()):
        if request.method == "POST":
            number = request.POST.get("number")
            message = request.POST.get("message")        
            print(request.POST)
            envio = scrapers.sendMessege(message, number)    
        return render(request, 'wp/sended.html', {'envio':envio})
    else:
        scrapers.importWhatsappQrCode()
        return render(request, 'wp/status.html')
    

def getLaudoNumber(laudo):
    #faço uma varredura dentro dos objectos e coloco o telefone na conta
    if laudo.cliente != None:               
        #pego o telefone da empresa ou do cliente.
        return laudo.cliente.whatsapp
    if laudo.empresa != None:
        return laudo.empresa.whatsapp      

def getDaysLeft(laudo):
    #faço o cálculo de quantos dias faltam    
    return (laudo.dataValidade-date.today()).days
