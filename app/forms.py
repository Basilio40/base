from django import forms
from .models import Obras

class ObrasForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ['nome','cep','logradouro','numero','complemento','bairro','estado','cidade','observacao','data_inicio','data_prevista']

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ['descricao_planta_baixa','descricao_planta_baixa1','planta_data','planta_data1','imagem_planta_baixa','imagem_planta_baixa1']