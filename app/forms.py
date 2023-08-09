from django import forms
from .models import Obras, Imagem

class ObrasForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ['nome','cep','logradouro','numero','complemento','bairro','estado','cidade','observacao','data_inicio','data_prevista']

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = '__all__'

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Imagem
        fields = '__all__'
            