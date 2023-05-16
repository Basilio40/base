from django import forms
from .models import Obras,Planta

class ObrasForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ['nome','cep','logradouro','numero','complemento','bairro','estado','cidade','observacao','data_inicio','data_prevista']

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = '__all__'