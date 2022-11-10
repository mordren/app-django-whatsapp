from django.shortcuts import render
import time
from clientes.models import Laudo
from gestor_laudo import scrapers
from django.shortcuts import get_object_or_404

def status(request):
    if (scrapers.whats_login()):
        return render(request, 'wp/status.html', {'status':True})
    else:        
        scrapers.importWhatsappQrCode()
        time.sleep(2)
        return render(request, 'wp/status.html', {'status':False})
 
def vencimento(request):
    laudos = Laudo.objects.all()                
    for laudo in laudos:
        #aqui eu estou adicionando esses atributos só para o FORM        
        laudo.telefone = Laudo.get_laudo_number(laudo)            
        laudo.vencimento = Laudo.get_days_left(laudo)        
    return render(request, 'wp/vencimento.html', {'laudos':laudos})

def prepareMessage(request, pk):
    laudo = get_object_or_404(Laudo, pk=pk)    
    #aqui eu estou adicionando esses atributos só para o FORM
    laudo.telefone = Laudo.get_laudo_number(laudo)            
    laudo.vencimento = Laudo.get_days_left(laudo)           
    laudo.mensagem = f"Olá estamos entrando em contato para lhe informar que o veículo: *{laudo.placa}*, estará com o *{laudo.tipo}* vencendo em {laudo.vencimento} dias. Venha à Agil Inspeções : Endereço bla bla bla, Palmas-TO. Abraço e tenha um bom dia"
    return render(request, 'wp/send.html',{'laudo':laudo})

def sendMessage(request):    
    if (scrapers.whats_login()):
        if request.method == "POST":
            number = request.POST.get("number")
            message = request.POST.get("message")                    
            envio = scrapers.send_messege(message, number)    
        return render(request, 'wp/sended.html', {'envio': envio})
    else:
        scrapers.importWhatsappQrCode()
        return render(request, 'wp/status.html')
    

