from wsgiref.validate import validator
from django.db import models
from django.urls import reverse_lazy
from django_cpf_cnpj.fields import CNPJField
from django.core.validators import MinValueValidator, MaxValueValidator

class Person(models.Model):
    name = models.CharField(max_length=60)    
    email = models.EmailField(blank=True, null=True)
    phone = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999)],
                help_text="DD-XXXX XXXX sem os espaços e sem o nove adicional",
                unique=True)
    sucess_url = reverse_lazy('home')    

class Empresa(models.Model):
    name = models.CharField(max_length=60)
    cnpj = CNPJField(masked=True)
    telefone = models.IntegerField(blank=True, null=True)   
    email = models.EmailField(blank=True, null=True)
    
class TipoLaudo(models.Model):
    tipoLaudo = models.CharField(max_length=10)

class Laudo(models.Model):    
    numero = models.IntegerField()
    tipo = models.ManyToManyField(TipoLaudo)
    cliente = models.ManyToManyField(Person, blank=True, null=True)
    empresa = models.ManyToManyField(Empresa, blank=True, null=True)
    dataValidade = models.DateField()
    observacoes = models.TextField(blank=True, null=True)    
    