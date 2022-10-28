from django.db import models
from phone_field import PhoneField

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=60)
    phone = PhoneField(blank=True, help_text='Contact Phone')
    email = models.EmailField(blank=True, null=True)
    
    

    #relação de um para um quando cada um objeto é ligado ao outro e não poderá ser ligado para outro.    
        