from django.db import models
from datetime import datetime

# Create your models here.
class Imagem(models.Model):
    img = models.FileField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url
    
    
class Obras(models.Model):
    
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=25, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField( null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    observacao = models.CharField(max_length=255, null=True, blank=True)
    data_inicio = models.DateField(auto_now=False, null=True, blank=True)
    data_prevista = models.DateField(auto_now=False, null=True, blank=True)
    # Arquitetonico
    descricao_planta_baixa = models.CharField(max_length=200, null=True, blank=True)
    planta_data = models.DateField(auto_now=False, null=True, blank=True)
    imagem_planta_baixa = models.FileField(upload_to='',null=True, blank=True)
    descricao_planta_baixa1 = models.CharField(max_length=200, null=True, blank=True)
    planta_data1 = models.DateField(auto_now=False, null=True, blank=True)
    imagem_planta_baixa1 = models.FileField(upload_to='',null=True, blank=True)
    
    
    def data_formatada(self):
        date = datetime.strptime(str(self.data_inicio), '%d-%m-%Y')
        return date
    
    def __str__(self):
        return self.nome
    

 
    # Estrutural

    #Hidraulico

    #Eletrico

    #Excepcionais

    
    # Laudos
    # Preliminar/Cautelar

    #Aterramento
   
    #Sondagem Solo
    # Arrancamento

    # Estanqueidade

    # Corpos de Prova

    # Escopo
    # Serviço a serem executados

    # Obrigações

    # Contratos

    #Cronogramas

    #Compras

    #Seviços

    # Portifolio

    




    

    