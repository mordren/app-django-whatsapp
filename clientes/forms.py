from django.forms import ModelForm
from .models import Laudo 
from django import forms
from django.forms import ModelForm

class DateForm(ModelForm):    
    class Meta():
        model = Laudo
        dataValidade = forms.DateTimeField(input_formats=['%d/%m/%Y'])
        fields = ['numero','tipo', 'dataValidade']           