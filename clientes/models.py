from datetime import date
from time import strftime
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MaxValueValidator, MinLengthValidator

class Person(models.Model):
    name = models.CharField(max_length=60)    
    email = models.EmailField(blank=True, null=True)  
    whatsapp = models.PositiveBigIntegerField(validators=[MaxValueValidator(99999999999)],
                help_text="DD-9XXXX XXXX sem os espaços",
                unique=True)
    sucess_url = reverse_lazy('home')    
    
    def __str__(self):
        return self.name
    
class Empresa(models.Model):
    name = models.CharField(max_length=60) 
    telefone = models.IntegerField(null=True, blank=True)
    whatsapp = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999)],
                help_text="DD-XXXX XXXX sem os espaços e sem o nove adicional",
                unique=True)    
    
    def __str__(self):
        return self.name

class Laudo(models.Model):
    CIPP = 'CIPP'
    CIV = 'CIV'    
    DATE_INPUT_FORMATS = ['%d/%m/%Y']
    numero = models.IntegerField(unique=True)    
    cliente = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True,
                help_text="Se não tem cliente deixar vazio")    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True,
                help_text="Se não tem empresa deixar vazio")   
    tipo = models.CharField(max_length=4, choices=[(CIV, 'CIV'),(CIPP, 'CIPP')])   
    dataLaudo = models.DateField()
    placa = models.CharField(help_text="formato XXX-XXXX", max_length=8)
    dataValidade = models.DateField()
    def __str__(self):
        return 'Laudo Nº' + str(self.numero) + ' Vencimento ' + self.dataValidade.strftime("%d/%m/%y")

    def get_laudo_number(self):
        #faço uma varredura dentro dos objectos e coloco o telefone na conta
        if self.cliente != None:               
            #pego o telefone da empresa ou do cliente.
            return self.cliente.whatsapp
        if self.empresa != None:
            return self.empresa.whatsapp      

    def get_days_left(self):
        #faço o cálculo de quantos dias faltam    
        return (self.dataValidade-date.today()).days

class Mensage(models.Model):    
    mensage = models.TextField() 
    phone = models.IntegerField()       
    type = models.CharField(max_length=10, choices=[('periodo1', '30 dias'),('periodo2', '15 dias')])   
    send = models.BooleanField(default=False)
    laudo = models.ForeignKey('Laudo', on_delete=models.CASCADE)
      
    def __str__(self):
        return self.mensage
    
    
    