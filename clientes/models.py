from wsgiref.validate import validator
from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MaxValueValidator

class Person(models.Model):
    name = models.CharField(max_length=60)    
    email = models.EmailField(blank=True, null=True)  
    phone = models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999)],
                help_text="DD-XXXX XXXX sem os espaços e sem o nove adicional")
    sucess_url = reverse_lazy('home')